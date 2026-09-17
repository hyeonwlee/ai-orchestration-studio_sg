import pandas as pd
pd.set_option("display.width", 180)

# CSV 로드 (한글 데이터: encoding 명시 습관!)
df = pd.read_csv("sales_sample.csv", encoding="utf-8")
# Excel 로드도 한 줄: pd.read_excel("inventory_sample.xlsx", sheet_name="재고현황")

# 탐색 루틴: 로드하면 무조건 이 4가지부터
print(" === sales_sample csv 파일 내용 === ")
print(df.head())       # 앞 5행 미리보기
print(df.shape)        # (행 수, 열 수)
print(df.info())       # 열 이름, 타입, 결측 여부
print(df.describe())   # 숫자 열의 기초 통계

# 단일 조건: 음료 카테고리만
drinks = df[df["category"] == "음료"]
print(" === drinks 데이터프레임 === ")
print(drinks.head())

# 다중 조건: 음료이면서 수량 100 이상 — 각 조건을 괄호로, &(그리고) |(또는)
hot = df[(df["category"] == "음료") & (df["quantity"] >= 3)]
print(" === hot 데이터프레임 === ")
print(hot.head())

# 특정 값 목록에 포함: isin
target = df[df["product"].isin(["아메리카노", "카페라떼"])]
print(" === target 데이터프레임 === ")
print(target.head())

# 매출액 = 단가 × 수량 : 열 전체에 대한 벡터 연산 (for문 불필요)
df["sales"] = df["unit_price"] * df["quantity"]
print(" === df 데이터프레임 (sales 추가)=== ")
print(df.head())

# 주문일자에서 '월' 추출 : 과제의 월별 집계에 필요
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month
print(" === df 데이터프레임 (month 추가)=== ")
print(df.head()) 

top = df.sort_values("sales", ascending=False)          # 매출액 내림차순
print(" === top 데이터프레임 (매출액 내림차순)=== ")
print(top.head()) 

multi = df.sort_values(["category", "sales"], ascending=[True, False])
print(" === multi 데이터프레임 (category 오름차순, sales 내림차순)=== ")
print(multi.head())   # 가–나-다 순으로 정렬 이후 매출액 내림차순

# 카테고리별 매출 합계
by_cat = df.groupby("category")["sales"].sum()
print(" === category 별 매출액 합계 === ")
print(by_cat.head())  

# 월별 × 카테고리별, 합계와 평균을 한 번에: agg
report = df.groupby(["month", "category"])["sales"].agg(
    총매출="sum", 평균매출="mean", 거래건수="count")
report = report.reset_index()   # 그룹 키를 일반 열로 되돌리기
print(report)

# CSV로 저장: index=False(행 번호 제외), Excel에서 열 파일은 utf-8-sig
report.to_csv("report.csv", index=False, encoding="utf-8-sig")

# Excel로 저장: 시트 여러 개를 한 파일에
with pd.ExcelWriter("Monthly_Report.xlsx", engine="openpyxl") as writer:
    report.to_excel(writer, sheet_name="월별요약", index=False)
    by_cat.reset_index().to_excel(writer, sheet_name="카테고리별", index=False)



