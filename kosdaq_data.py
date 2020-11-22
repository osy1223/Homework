import numpy as np
import pandas as pd
from pandas import DataFrame

# csv 파일 불러오기 (인코딩 주의)
kosdaq = pd.read_csv('./data/코스닥.csv',
            header=0, index_col=0, sep=',', encoding='cp949')

print('kosdaq:',kosdaq)

print("kosdaq value category:",set(kosdaq))

# # 일부 데이터만 가져오기
kosdaq = kosdaq[['고가','저가','시가']]
print(kosdaq)


# 일자 기준으로 오름차순으로 변경
kosdaq = kosdaq.sort_values(['일자'], ascending=['True'])
print(kosdaq)

# row 맞춰주기
kosdaq = kosdaq.iloc[39:659]
print(kosdaq)
# [620 rows x 3 columns]


'''
#콤마 제거 후 문자를 정수로 변환
for i in range(len(kosdaq.index)):
    for j in range(len(kosdaq.iloc[i])):
        kosdaq.iloc[i,j] = int(kosdaq.iloc[i,j].replace('.',''))
print(kosdaq)
'''
