import pandas as pd
file_name='142801_20230105190308879_excel.xlsx'
df=pd.read_excel(file_name, skiprows=2, nrows=2, index_col=0)
df

# df.loc['출생아 수'] # 에러가 뜸
df.index # index 이름이 맞는데 에러가 뜸
df.index.values # 자세히 살펴보니 사이에 유니코드가 끼워져 있음을 알 수 있음. 즉 변환 필요

df.rename(index={'출생아\xa0수':'출생아 수', '합계\xa0출산율':'합계 출산율'}, inplace=True)
df.index.values

df.loc['출생아 수'] 
df.iloc[0] # 위와 똑같은 결과를 출력
df.iloc[1]

df.T # row와 col을 변환
df= df.T
df

# 시각화

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic' # Windows 폰트
matplotlib.rcParams['font.size']=15 # 폰트 크기
matplotlib.rcParams['axes.unicode_minus']=False # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

plt.plot(df.index, df['출생아 수']) # 꺽은 선 그래프 출력(x축, y축)
plt.plot(df.index, df['합계 출산율'])

fig, ax1=plt.subplots(figsize=(10,7)) # 가로 세로 크기 지정
ax1.plot(df.index, df['출생아 수'], color='#ff812d') # ax1 색깔 지정

ax2=ax1.twinx() # y값은 서로 다르지만 x축을 공유하는 axis
ax2.plot(df.index, df['합계 출산율'], color='#ffd100')

fig, ax1=plt.subplots(figsize=(13,5)) # 그래프 가로 세로 크기 조절
ax1.set_ylabel('출생아 수(천명)') # ax1의 y 제목을 지음
ax1.set_ylim(250,700) # ax1의 범위를 250~700으로 지정
ax1.set_yticks([300,400,500,600]) # 300, 400, 500, 600 만 표기
ax1.bar(df.index, df['출생아 수'], color='#ff812d')

ax2=ax1.twinx() # x축을 공유하는 axis
ax2.set_ylabel('합계 출산울(가임여성 1명당 명)')
ax2.set_ylim(0,1.5)
ax2.set_yticks([0,1])
ax2.plot(df.index, df['합계 출산율'], color='#ffd100')

fig, ax1=plt.subplots(figsize=(13,5))
ax1.set_ylabel('출생아 수(천명)')
ax1.set_ylim(250,700)
ax1.set_yticks([300,400,500,600])
ax1.bar(df.index, df['출생아 수'], color='#ff812d')
for idx, val in enumerate(df['출생아 수']): # idx변수는 df['출생아 수']의 index값을 가지고, val변수는 df['출생아 수']의 값을 가지는 반복함수 변수이다.
    ax1.text(idx,val+12, val, ha='center') # 변수는 text형태로 그래프에 나타내고 그래프보다 12만큼 위에, val을 센터(중앙)에 출력한다.
    

ax2=ax1.twinx() # x축을 공유하는 axis
ax2.set_ylabel('합계 출산울(가임여성 1명당 명)')
ax2.set_ylim(0,1.5)
ax2.set_yticks([0,1])
ax2.plot(df.index, df['합계 출산율'], color='#ffd100')

fig, ax1=plt.subplots(figsize=(13,5))
fig.suptitle('출생아 수 및 합계출산율')
ax1.set_ylabel('출생아 수(천명)')
ax1.set_ylim(250,700)
ax1.set_yticks([300,400,500,600])
ax1.bar(df.index, df['출생아 수'], color='#ff812d')
for idx, val in enumerate(df['출생아 수']):
    ax1.text(idx,val+12, val, ha='center')
    

ax2=ax1.twinx() # x축을 공유하는 axis
ax2.set_ylabel('합계 출산울(가임여성 1명당 명)')
ax2.set_ylim(0,1.5)
ax2.set_yticks([0,1])
ax2.plot(df.index, df['합계 출산율'], color='#ffd100', marker='o', ms=10, lw=5, mec='w', mew=1.5) # 색깔, 꼭짓점, 꼭짓점 크기, 선 크기, 꼭짓점 테두리 색깔, 꼭짓점 테두리 사이즈 순서대로이다.
for idx, val in enumerate(df['합계 출산율']):
    ax2.text(idx, val + 0.08, val, ha='center')