# KBO 정규시즌 승률 예측 - 선형회귀 모델
- KBO 2003~2023 시즌 데이터를 활용해 정규시즌 최종 승률을 예측하는 선형회귀 모델


## Overview
- 한국프로야구(kbo) 타격·투수·수비 지표 데이터를 분석하여
  **승률에 영향을 주는 핵심 요소를 파악**하고, OLS 선형회귀 모델로 정규시즌 최종 승률을 예측

### Problem Definiton
```
f : OLS 선형회귀 모델
x : KBO 순위에 영향을 주는 타격·투수·수비 지표 (44개 변수)
y : 정규시즌 최종 승률 (WP)
```

---

## Data

| 항목 | 내용 |
|------|------|
| 출처 | koreabaseball (KBO 공식 데이터) |
| 수집 기간 | 2003 ~ 2023 시즌 |
| 변수 수 | 총 44개 (타격, 투수, 수비 지표) |
| 파일 | `data/kbostats.csv` |

---

## Pipeline
```
데이터 수집 (KBO 타격·투수·수비 지표)
    ↓
1차 변수 선정 (상관관계 기반 필터링 + 도메인 지식)
    ↓
2차 변수 선정 (다중공선성 제거 — VIF 분석)
    ↓
OLS 모델 학습 (train 80 / test 20)
    ↓
모델 성능 평가 및 회귀식 도출
```

---

## Preprocessing

**1차 변수 선정**
- 종속변수(승률)와 각 설명변수 간 상관관계 계산
- 상관계수 0.2 이하 변수 제거
- 도메인 지식 + 선행 논문 기반 추가 변수 제거
- 1차 선정 변수: `AVG` `R` `H` `HR` `TB` `RBI` `SF` `BB` `IBB` `HPB` `OBP` `SLG` `OPS` `SB` `SV` `HLD`

**2차 변수 선정 (중복 제거)**

| 제거 변수 | 제거 이유 |
|----------|----------|
| AVG, SLG, OBP | OPS와 중복 |
| H, HR | TB에 포함 |
| RBI | R과 중복 (선행연구 참고) |

**최종 선정 변수 (11개)**
`R` `SF` `BB` `IBB` `HPB` `OPS` `SB` `SV` `HLD`

---
 
## Model

**OLS (Ordinary Least Squares)**

| 항목 | 내용 |
|------|------|
| Train / Test | 80% / 20% |
| VIF 처리 | TB(총루타) 제거 — R과 다중공선성 존재 |
| 최종 변수 수 | 10개 |
| **R-Squared** | **0.681** |

### 최종 회귀식
```
WP = 0.5011
   + 0.045  × SV  (세이브)
   + 0.0196 × OPS (출루율+장타율)
   + 0.0114 × SF  (희생플라이)
   + ...
```

---
 
## Insight

- **세이브(SV)** 가 승률에 가장 큰 영향 → 마무리 투수 운용이 승리에 핵심적
- **OPS** 는 타격 지표 중 승률 예측력이 가장 높은 변수
- **변수 선정 방식의 한계** : 상관관계 기반 필터링만으로는 최적 변수 조합을 보장할 수 없음
- **개선 방향** : Lasso/Ridge 회귀, 전진·후진 선택법 등 다양한 변수 선정 방법론 비교 필요

---

## Tech Stack

| Category | Stack |
|----------|-------|
| 모델 | OLS (statsmodels) |
| 다중공선성 검사 | VIF (variance_inflation_factor) |
| 데이터 처리 | pandas, numpy |
| 환경 | Google Colab, Python 3.10.12 |

---

## Project Structure
```
├── code/
│   ├── preprocessing/
│   │   └── 1차 설명변수 선정.py
│   └── modeling/
│       ├── OLS_training+analysis.py
│       └── vif+feature selection.py
├── data/
│   └── kbostats.csv
└── README.md
```
