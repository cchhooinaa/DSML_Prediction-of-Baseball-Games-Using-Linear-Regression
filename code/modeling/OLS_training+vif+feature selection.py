# 표준화 진행
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scale_columns =[ 'R', 'TB', 'SF', 'BB', 'IBB', 'HPB', 'OPS', 'SB', 'SV', 'HLD']
df[scale_columns] = scaler.fit_transform(df[scale_columns])

numerical_columns=[ 'R', 'TB', 'SF', 'BB', 'IBB', 'HPB', 'OPS', 'SB', 'SV', 'HLD']


# train/test set 나누기
from sklearn.model_selection import train_test_split

X = df[numerical_columns]
y = df['WP']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)


# 다중공선성 존재 여부 확인
from statsmodels.stats.outliers_influence import variance_inflation_factor

vif = pd.DataFrame()
vif['features'] = X_train.columns
vif["VIF Factor"] = [variance_inflation_factor(X_train.values, i) for i in range(X_train.shape[1])]
vif.round(1)

# R(득점), TB(총루타) 변수에 다중공선성 존재
# 최종 설명변수 선정_Pearson 상관계수 활용
cols = [ 'R', 'TB', 'SF', 'BB', 'IBB', 'HPB', 'OPS', 'SB', 'SV', 'HLD']

corr = df[cols].corr(method = 'pearson')
corr

# HeatMap을 통해 설명변수 간의 상관관계 확인
fig = plt.figure(figsize = (12, 10))
ax = fig.gca()

sns.set(font_scale = 1.0)
heatmap = sns.heatmap(corr.values, annot = True, fmt='.2f', annot_kws={'size':15},
                      yticklabels = cols, xticklabels = cols, ax=ax, cmap = "RdYlBu")
plt.tight_layout()
plt.show
# R(득점)과 TB(총루타)이 높은 상관관계를 보임
# R(득점)변수와 높은 상관관계를 보이는 변수가 많음 + 선행연구 참고 -> R(득점) 변수 제거

# 최종 변수
# 총 10개의 변수
# R(득점) SF(희생플라이) BB(4구) IBB(고의4구) HPB (사구) OPS(출루율+장타율) SB(도루허용) SV(세이 브) HLD (홀드)
