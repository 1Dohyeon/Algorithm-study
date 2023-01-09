# 인구 피라미드

import pandas as pd

# 남자 데이터 정의

file_name='202212_202212_연령별인구현황_월간.xlsx'
df_m=pd.read_excel(file_name, skiprows=3, index_col='행정기관', usecols='B, E:Y')
# excel형태의 데이터를 불러옴, 위에 row 3개를 skip(삭제)한 채로 불러옴, '행정기관'을 index로 설정, excel파일의 B열, E~Y열까지 불러옴)
df_m.head(3) # 위에 row 3개만 불러옴

df_m.iloc[0] # 숫자 사이에 , 때문에 타입이 문자열임, int로 변환 필요

df_m.iloc[0]=df_m.iloc[0].str.replace(',','').astype(int) # 데이터에 있는 , 를 공백으로 변환하고 데이터 타입을 int로 변환
df_m.iloc[0]

# 여자 데이터 정의

df_w=pd.read_excel(file_name, skiprows=3, index_col='행정기관', usecols='B, AB:AV')
df_m.head(3)

df_w.columns=df_m.columns # 컬럼명 통일
df_w.columns

df_w.iloc[0]=df_w.iloc[0].str.replace(',','').astype(int)
df_w

# 데이터 시각화

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic' # Windows 폰트
matplotlib.rcParams['font.size']=15 # 폰트 크기
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

plt.figure(figsize=(10,7))
plt.barh(df_m.columns, -df_m.iloc[0] // 1000) 
# bar는 막대그래프를 시각화, barh는 가로 방향 막대그래프(col을 y축에 배치, df_m[0]만 그래프에 생성(-를 붙여 방향을 반대로 취함), 단위: 천 명)
# 원래 괄호 안에 x축, y축 순서지만 barh로 뒤집어졌기 때문에 y축이 col값인거다.
plt.barh(df_w.columns, df_w.iloc[0] // 1000)
plt.title('2022 대한민국')
plt.savefig('2022_인구피라미드.png', dpi=100)
plt.show()

plt.figure(figsize=(10,7))
plt.barh(df_m.columns, df_m.iloc[0] // 1000) # bar는 막대그래프를 시각화, barh는 가로 방향 막대그래프(단위: 천 명)
plt.barh(df_w.columns, df_w.iloc[0] // 1000)
plt.title('2022 대한민국')
plt.show()

# 평범한 막대 그래프
plt.figure(figsize=(30,15))
plt.bar(df_m.columns, df_m.iloc[0] // 1000) 
plt.bar(df_w.columns, df_w.iloc[0] // 1000)
plt.title('2022 대한민국')
plt.show()

# 여자 그래프와 남자 그래프를 합하여 총 인구수 구하기
plt.figure(figsize=(30,15))
plt.bar(df_m.columns, df_m.iloc[0] // 1000, bottom=df_w.iloc[0] // 1000) 
plt.bar(df_w.columns, df_w.iloc[0] // 1000)
plt.title('2022 대한민국')
plt.show()