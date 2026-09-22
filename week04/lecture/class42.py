import pandas as pd
df = pd.read_csv("dirty_sales.csv", encoding="utf-8")

print(df.shape)                       # (행, 열) 크기
print(df.info())                      # 컬럼별 non-null 개수와 dtype 한눈에
print(df.isna().sum())                # 컬럼별 결측치 개수
print(df[df["price"].isna()].head())  # 결측이 있는 행 직접 눈으로 확인

# =====

# "4,500", "4500원", "" 이 섞인 지저분한 컬럼의 정석 처리
df["price"] = (df["price"].astype(str)			# 문자열로 강제 변환
                          .str.replace(＂,＂, ＂＂)		# 콤마를 없애고
                          .str.replace(＂원＂, ＂")		# 원 문자가 있으면 없애고
                          .str.strip())			# 문자열의 맨 앞(Leading)과 맨 뒤(Trailing) 탭이나 공백 제거
df["price"] = pd.to_numeric(df["price"], errors="coerce")  	# 변환 불가한 경우 NaN으로 대체
print(df["price"].isna().sum())   # coerce로 새로 생긴 NaN 개수 반드시 재확인

# =====

print(df["price"].describe())
# count      498.0
# mean     12840.5    ← 평균이 상식보다 크다?
# min       -4500.0   ← 음수 가격!
# max     9999999.0   ← 입력 오류로 의심되는 극단값

print(df.sort_values("price").head(5))   # 최소값 쪽 실제 행 확인
print(df.sort_values("price").tail(5))   # 최대값 쪽 실제 행 확인

q1 = df["price"].quantile(0.25)
q3 = df["price"].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
outliers = df[(df["price"] < lower) | (df["price"] > upper) | (df["price"] < 0)]
print(f"이상치 {len(outliers)}건 / 전체 {len(df)}건")
print(outliers)

