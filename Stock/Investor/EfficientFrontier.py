import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import Analyzer
from datetime import datetime

# 시총 상위 종목 효율적 투자선 구해보기
# 삼성전자 액면분할 = 2018-05-04
# 네이버 액면분할 = 2018-10-12
# 그래서 우리는 2018-10-12 ~ 오늘
mk = Analyzer.MarketDB()
stocks = ['삼성전자', 'SK하이닉스', 'NAVER', 'LG화학', '현대자동차']
df = pd.DataFrame()
for s in stocks:
    today = datetime.today().strftime('%Y-%m-%d')
    df[s] = mk.get_daily_price(s, '2018-10-12', today).close

# 각 종목 비교하기 위해 일간 변동률 비교!
# pandas DataFrame이 제공해주는 pct_change() 사용
daily_ret = df.pct_change()
'''
            삼성전자  SK하이닉스   NAVER    LG화학 현대자동차
date                                                        
2018-10-12       NaN       NaN       NaN       NaN       NaN
2018-10-15 -0.004545 -0.029006 -0.042254  0.028526 -0.017316
2018-10-16 -0.004566 -0.008535 -0.018382 -0.018490  0.026432
2018-10-17  0.012615  0.010043 -0.026217  0.020408  0.017167
2018-10-18 -0.002265 -0.024148 -0.038462 -0.024615 -0.021097
              ...       ...       ...       ...       ...
2021-03-10 -0.006143 -0.025641  0.029046  0.034843 -0.017279
2021-03-11  0.013597  0.030075  0.004032  0.053872  0.004396
2021-03-12  0.009756  0.021898  0.018742  0.005325  0.017505
2021-03-15 -0.012077 -0.025000  0.006570  0.023305 -0.002151
2021-03-16  0.012225  0.029304  0.006527 -0.077640  0.008621
[598 rows x 5 columns]
'''

# 연간 수익률 우리나라 평균 개장일 : 2020년 248일 / 2019년 246일
# 깔끔하게 250일로 설정
annual_ret = daily_ret.mean() * 250
'''
삼성전자      0.304919
SK하이닉스    0.353203
NAVER     0.490067
LG화학      0.532772
현대자동차     0.380482
dtype: float64
'''

# 일간 리스크는 cov() 함수를 사용해 일간 변동률의 공분산으로 구한다.
daily_cov = daily_ret.cov()
'''
           삼성전자  SK하이닉스  NAVER     LG화학  현대자동차
삼성전자    0.000323  0.000323  0.000138  0.000222  0.000227
SK하이닉스  0.000323  0.000609  0.000176  0.000256  0.000245
NAVER       0.000138  0.000176  0.000579  0.000218  0.000173
LG화학      0.000222  0.000256  0.000218  0.000787  0.000271
현대자동차  0.000227  0.000245  0.000173  0.000271  0.000694
'''

# 연간 공분산은 일간 리스크에서 250 곱하기
annual_cov = daily_cov * 250
'''
           삼성전자  SK하이닉스   NAVER    LG화학  현대자동차
삼성전자    0.080645  0.080796  0.034624  0.055427  0.056674
SK하이닉스  0.080796  0.152298  0.044055  0.064092  0.061336
NAVER       0.034624  0.044055  0.144832  0.054514  0.043218
LG화학      0.055427  0.064092  0.054514  0.196821  0.067827
현대자동차  0.056674  0.061336  0.043218  0.067827  0.173495
'''

'''
몬테카를로 시뮬레이션
시총 상위 5종목으로 구성된 포트폴리오 20,000개 생성
난수를 사용해, 함수의 값을 확률적으로 계산하는 방식을 몬테카를로 시뮬레이션
'''

# 포트폴리오 20000개 생성
port_return = []  # 포트폴리오 수익률
port_risk = []  # 포트폴리오 리스크
port_weights = []  # 포트폴리오의 각 종목 비중
sharp_ratio = []  # 샤프 지수 (측정된 위험 단위당 수익)

for _ in range(20000):
    weights = np.random.random(len(stocks))  # ==> (5,)
    weights /= np.sum(weights)  # ==> 각 weights값의 합이 1이 되도록 만들기 위해!

    # 랜덤하게 생성한 종목별 비중 배열과 종목별 연간 수일률을 곱해 해당 포트폴리오의 수익률 구함
    # 포트폴리오의 수익률
    returns = np.dot(weights, annual_ret)

    # [종목별 연간 공분산(annual_cov) * 종목별 비중(weights)] * 종목별 비중의 전치(weights.T)
    # 이렇게 구한 결과값의 제곱근 == 해당 포트폴리오의 전체 리스크
    risk = np.sqrt(np.dot(weights.T, np.dot(annual_cov, weights)))

    # 포트폴리오 20,000개  수익률, 리스트, 종목비중을 리스트에 담는다.
    port_return.append(returns)
    port_risk.append(risk)
    port_weights.append(weights)
    sharp_ratio.append(returns/risk)

portfolio = {'Returns': port_return, 'Risk': port_risk, 'Sharp': sharp_ratio}

for idx, val in enumerate(stocks):
    # 각 종목의 종목 비중 column을 추가
    portfolio[val] = [weight[idx] for weight in port_weights]

df = pd.DataFrame(portfolio)
df = df[['Returns', 'Risk', 'Sharp'] + [s for s in stocks]]

# 포트폴리오 중에서 측정된 위험 단위당 수익이 제일 높은 포트폴리오
max_sharp = df.loc[df['Sharp'] == df['Sharp'].max()]
min_risk = df.loc[df['Risk'] == df['Risk'].min()]

# 컬러맵 = viridis / 테두리 색 = 검정색(k)
df.plot.scatter(x='Risk', y='Returns', c='Sharp', cmap='viridis',
                edgecolors='k', figsize=(10,7), grid=True)
# plt.title('Efficient Frontier')  # >>> 효율적 투자선 구할 때 제목

# 샤프 지수가 가장 큰 포트폴리오를 300 크기의 붉은 별표로 표시
plt.scatter(x=max_sharp['Risk'], y=max_sharp['Returns'], c='r', marker='*', s=300)

# 리스크가 제일 작은 포트폴리오를 200 크기의 붉은 x표
plt.scatter(x=min_risk['Risk'], y=min_risk['Returns'], c='r', marker='X', s=200)

plt.title('Portfolio Optimization')
plt.xlabel('Risk')
plt.ylabel('Expected Returns')
plt.show()

print(max_sharp)  # <<< 샤프 지수(위험단위당 수익률)가 가장 큰
'''
      Returns     Risk     Sharp   삼성전자  SK하이닉스   NAVER      LG화학   현대자동차
9732  0.446941  0.277036  1.613297  0.21811   0.04085    0.408824   0.234407   0.097808
'''

print(min_risk)  # <<<< 가장 위험률이 적은 포트폴리오
'''
      Returns      Risk     Sharp   삼성전자   SK하이닉스    NAVER      LG화학     현대자동차
2662   0.3793  0.255518  1.484437    0.54021     0.01098    0.242977   0.068466     0.137373
'''