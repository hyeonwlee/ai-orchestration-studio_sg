# -*- coding: utf-8 -*-
"""
buggy_1.py  ―  판매 데이터 매출 집계 (csv 모듈 버전)

dirty_sales.csv를 한 줄씩 읽어 '매출액 = 단가 x 수량'을 누적한다.
잘 돌아가는 것처럼 보이지만, 어떤 행에서 갑자기 멈춘다.

[과제] 이 스크립트를 실행해 Traceback을 얻고,
       진단 3단계 루틴(무엇이 / 어디서 / 왜)으로 원인을 특정한 뒤
       전처리로 해결하라. (힌트: 예외 타입은 무엇인가?)
"""
import csv

def calc_total(path):
    total = 0
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)  # 사전타입으로 데이터를 읽음.
        for i, row in enumerate(reader):
            if row["price"].strip() == "": price = 0                          # FIXED: 결측치의 경우 0으로 치환하였다.
            else: price = int(row["price"].replace(",","").replace("원",""))  # FIXED: 숫자 문자열을 int()가 정수로 올바로 변환할 수 있도록, 문자열에 포함된 숫자 이외의 문자를 빈 문자열로 치환하게 하였다.
            qty = int(row["quantity"])
            total += price * qty
    return total

if __name__ == "__main__":
    total = calc_total("./dirty_sales.csv")
    print(f"총 매출액: {total:,}원")