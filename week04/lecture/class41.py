order = {"product": "라떼", "price": 5500}
print(order["amount"])          # KeyError: 'amount'

import pandas as pd
df = pd.read_csv("sales.csv", encoding="cp949")    # 헤더: Product, Price
df["price"].sum()               # KeyError: 'price' (대소문자 불일치)

price = "4500"          # CSV에서 읽으면 문자열인 경우가 많다
total = price + 500     # TypeError: can only concatenate str (not "int") to str

len(12345)              # TypeError: object of type 'int' has no len()

int("4,500")     # ValueError: invalid literal for int() with base 10: '4,500'
int("")          # ValueError (빈 문자열)
int("4500원")    # ValueError (단위 문자 포함)

rows = ["헤더", "1행", "2행"]
print(rows[3])          # IndexError: list index out of range
last = rows[len(rows)]  # 마지막 원소를 원했다면 rows[-1] 또는 rows[len(rows)-1]

name = "latte"
name.append("!")        # AttributeError: 'str' object has no attribute 'append'

result = df[df["price"] > 10000]
top = result.sort_value("price")   # AttributeError: ... no attribute 'sort_value'
                                   # 올바른 이름은 sort_values (s 누락 오타)

data = load_config()    # 함수가 return을 잊어 None을 반환
data.keys()             # AttributeError: 'NoneType' object has no attribute 'keys'
