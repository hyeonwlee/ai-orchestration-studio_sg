import pandas as pd
from classify import classify_review

df = pd.read_csv("reviews_sample.csv")
reviews = df["review_text"]

success_cnt = 0
failure_cnt = 0
data_stats = {}
for r in reviews:
    data, description = classify_review(r)
    data_stats[description] = data_stats.get(description, 0) + 1
    if data is None: failure_cnt += 1
    else: success_cnt += 1

print(f"처리 {success_cnt}건 / 실패 {failure_cnt}건")

print("집계 결과 통계:")
for description in sorted(data_stats):
    print(f"{description}: {data_stats[description]}")