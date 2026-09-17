import csv

# DictReader: 각 행을 딕셔너리로 읽는다 (헤더가 key)
with open("sales_sample.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    sales_summary = {}
    for row in reader:
        product = row["product"]
        amount = int(row["unit_price"]) * int(row["quantity"])
#      print(f"{row["product"]}: {amount:,}원")
        if product not in sales_summary: 
            sales_summary[product] = 0
        sales_summary[product] += amount

# 상품별 Summary 출력
print("\n===== 상품별 매출 Summary =====")
for product, amount in sales_summary.items():
    print(f"{product}: {amount:,}원")

# DictWriter에 넣기 위한 리스트 생성
summary = []
for product, amount in sales_summary.items():
    summary.append( {"상품명": product, "매출액": amount} )

# summary.csv 파일로 저장
with open("summary.csv", "w", encoding="utf-8-sig", newline="") as f:
# utf-8-sig: 이 파일이 utf-8 이라는 표식, BOM(Byte Order Mark)을 파일 맨 앞에 추가
# newline="": csv 파일을 저장할 때 줄 바꿈을 null로 지정하여 csv 모듈에서 직접 처리
    writer = csv.DictWriter(f, fieldnames=["상품명", "매출액"])
    writer.writeheader()  # 첫 번째 행에 변수명 기록
    writer.writerows(summary)  # 실제 데이터 기록
print("summary.csv 파일 저장 완료")
