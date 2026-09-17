import json
with open("config_sample.json", "r", encoding="utf-8") as f:
    config = json.load(f)                    # dict로 변환됨
print(config["store"])                       # 신촌점
print(config["open_hours"]["weekend"])       # 09:00-21:00
for item in config["menu"]:                  # 리스트 순회
    print(item["name"], item["price"])
config["menu"].append({"name": "콜드브루", "price": 5200, "tags": ["신제품"]})
with open("config_updated.json", "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)
