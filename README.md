# DSML_Prediction of Baseball Games Using Linear Regression
- 2024년 3학년 1학기 머신러닝기반데이터분석 개인 프로젝트 아카이빙 레포지토리


## Project Information
- 한국프로야구(kbo)의 데이터를 활용해 정규시즌 승률을 예측하는 선형회귀모델 만들기
- 머신러닝모델링 중 회귀모델링을 통해, 승률에 영향을 주는 요소를 파악하고, 정규시즌 최종 승률을 예측
- y = f(x)
- y: 승률
- x: 순위에영향을주는요소들
- f: 회귀모델링(regression)

## 1. Development Environment
- Google Colaboratory
- python 3.10.12

## 2. Project Pipeline

## 3. Data
> koreabaseball(kbo)에서 수집
- 2003-2023 시즌의 최종 승률 및 타격, 투수, 수비 지표 데이터 수집
- 총 44개의 변수

## 4. Pre-processing
- 설명변수 선정
  - 종속변수와 각 설명변수 간의 상관관계 계산
  - 상관관계가 0.2 이하인 변수 제거
  - 도메인 지식을 활용해 추가적으로 변수 제거(논문 참고)
    
- 1차적으로 선정한 변수
  - AVG(타율) R(득점) H(안타) HR(홈런) TB(총루타) RBI(타점) S F ( 희 생 플 라 이 ) B B ( 4 구) 1 B B ( 고 의 4 구) H P B ( 사 구 ) O B P ( 출 루 율 ) SLG(장타율) OPs (출루율+장타율) SB(도루허용) SV(세이브) HLD(홀드)

- 추가적으로 제거할 설명변수 선정
  - AVG(타율), SLG(장타율),0BP(출루율) -> 0PS(장타율+출루율)와 중복되는 변수이므로 제거
  - H(안타)와 HR(홈런) -> TB(총루타) 변수가 포함하고 있으므로 제거
  - R(득점)과 RB(타점)는 중복되는 변수 -> RBI 제거 (선행연구 참고)

- 추가 제거 후 선정된 변수 리스트
  - A VG(타율)R(득점) TB(총루타) RP(타점) S F(희생플라이)B B(4구) 1BB(고의4구) HPB(사구) o p s ( 출 루 율 + 장 타 율) S B ( 도 루 허 용) S V( 세 이 브) H L D ( 홀 드)
 
## 5. Model
- train / test data
  - train: 8
  - test: 2
 
- VIF 확인
  - R(득점), TB(총루타) 변수에 존재
  - TB(총루타) 변수 제거 (선행연구 참고)

- 최종 변수 선정
  - AVG(타율) R(득점) SF(희생플라이) BB(4구) 1BB(고의4구) H P B ( 사구 ) o p s ( 출루 율+ 장 타 율 ) S B ( 도 루 허 용 ) S V ( 세이 브 ) H L D ( 홀드 )
  - 총 10개의 변수
 
- 모델 선정
  - OLS
 
- 모델 성능
  - R-Squared 0.681
 
- 최종 회귀식
  - WP(승률)=0.5011+0.045*SV(세이브) +0.0196*OPs(장타율+출루율) +0.0114*SF(도루허용) +...
 
## 6. Insight
- 변수 선정 방식의 한계
- 변수 선정 방식에 따른 모델 성능 비교 필요
  
