# 최종 변수 선정 후 모델링 과정 다시 진행
numerical_columns = ['R', 'SF', 'BB', 'IBB', 'HPB', 'OPS', 'SB', 'SV', 'HLD']

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scale_columns = ['R', 'SF', 'BB', 'IBB', 'HPB', 'OPS', 'SB', 'SV', 'HLD']
df[scale_columns] = scaler.fit_transform(df[scale_columns])

from sklearn.model_selection import train_test_split

X = df[numerical_columns]
y = df['WP']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

from sklearn import linear_model

# fit regression model in training set
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)

# predict in test set
pred_test = lr.predict(X_test)

# 모델해석하기

# 계수 출력
print(lr.coef_)

# "feature - coefficients" DataFrame 만들기
coefs = pd.DataFrame(zip(df[numerical_columns].columns, lr.coef_), columns = ['feature', 'coefficients'])
coefs

# 크기 순서대로 나열
# 절대값 기준 함수: coefficients.abs().sort_values
coefs_new = coefs.reindex(coefs.coefficients.abs().sort_values(ascending=False).index)
coefs_new

# coefficients 를 시각화

# figure size
plt.figure(figsize = (8, 8))

# bar plot
plt.barh(coefs_new['feature'], coefs_new['coefficients'])
plt.title('"feature - coefficient" Graph')
plt.xlabel('coefficients')
plt.ylabel('features')
plt.show()

# 유의성 검정
import statsmodels.api as sm

X_train2 = sm.add_constant(X_train)

model2 = sm.OLS(y_train, X_train2).fit()
model2.summary()

# 모델 결과 시각화
plt.figure(figsize=(12, 9))
plt.scatter(df.index, df['prediction'], marker='x', color='r')
plt.scatter(df.index, df['actual'], alpha=0.3, marker='o', color='black')
plt.title("Prediction Result in Test Set", fontsize=20)
plt.legend(['prediction', 'actual'], fontsize=12)
plt.show()

# 최종 결과 해석
0.699로 모델이 주어진 데이터에 대해 약 69.9%의 변동성을 설명

"R"(득점: p-value: 0.435),
“SF"(희생플라이: p-value:0.457),
"BB"(볼넷: p-value: 0.317),
"HLD"(홀드:0.826)는 유의하지 않음 (p value > 0.05)

[Positive] 변수 설명 : 승률에 Positive한 영향을 미침. 즉, 다른 변수의 값이 고정했을 때, 해당 변수의 값이 클수록 승률이 높을 것

"SF"(희생플라이),
"IBB"(고의4구),
"HPB"(사구),
"OPS"(출루율+장타율)
"SB"(도루허용)
"SV"(세이브)
[Negative] 변수 설명 : 승률에 Negative한 영향을 미침. 즉, 다른 변수의 값이 고정했을 때, 해당 변수의 값이 작을수록 승률이 높을 것

"HLD"(홀드)
