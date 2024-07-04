# 종속변수와 각 설명변수 간의 상관관계 계산
  상관관계가 0.2 이하인 변수 제거

cols = ['AVG', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'TB', 'RBI', 'SAC', 'SF', 'BB', 'IBB', 'HPB', 'SO', 'GDP',
       'SLG', 'OBP', 'OPS', 'SB', 'CS', 'ERA', 'SV', 'HLD', 'IP', 'H/p',
       'HR/p', 'BB/p', 'HBP', 'SO/p', 'R.1', 'ER', 'WHIP', 'E', 'PO', 'Ass',
       'DP', 'FPCT', 'PB', 'SB/f', 'CS/f', 'CS%']
y = 'WP'

correlation_matrix = df[cols].corrwith(df[y])

threshold = 0.2
low_correlation_variables = correlation_matrix[abs(correlation_matrix < threshold)].index
df = df.drop(low_correlation_variables, axis=1)

print(df.columns)
print('제거된 변수:', low_correlation_variables)
