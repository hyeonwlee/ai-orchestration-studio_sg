import pandas as pd

# 1. RAW_DATA.csv를 올바른 인코딩으로 로드하고, shape과 info() 확인한다.
for enc in ("utf-8", "cp949"):
    try:
        df = pd.read_csv("RAW_DATA.csv", encoding=enc)
        break
    except UnicodeDecodeError:
        continue
else: 
    raise ValueError("지원하지 않는 인코딩입니다.")

'''
print("=== RAW_DATA.csv 파일 정보 ===")
print("1. (행 수, 열 수) 확인:", df.shape)
print("2. 각 열의 이름, 타입, 결측치 여부 확인:"); df.info()
'''

'''
=== RAW_DATA.csv 파일 정보 ===
1. (행 수, 열 수) 확인: (500, 5)
2. 각 열의 이름, 타입, 결측치 여부 확인:
<class 'pandas.DataFrame'>
RangeIndex: 500 entries, 0 to 499
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   주문일자    500 non-null    str  
 1   상품명     500 non-null    str  
 2   카테고리    500 non-null    str  
 3   단가      500 non-null    str  
 4   수량      500 non-null    int64
dtypes: int64(1), str(4)
memory usage: 19.7 KB
'''
