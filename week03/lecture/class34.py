import json
# 1) 읽기: JSON 파일 → 파이썬 dict
with open("config_sample1.json", "r", encoding="utf-8") as f:
    config = json.load(f)

print(type(config))                       # <class 'dict'>
print(config["app_name"], config["version"]) # CafeSalesDashboard 1.3.0

# 2) 중첩된 값 접근: dict 안의 dict
db = config["database"]
print(f"DB 접속 주소: {db['host']}:{db['port']}/{db['name']}")
print("SSL 사용 여부:", db["use_ssl"])     # JSON의 false → 파이썬 False

# 3) 없는 키를 안전하게 읽기: get(키, 기본값)
# config["timeout"] 은 KeyError, config.get(...)은 기본값 반환
timeout = config.get("timeout", 30)
print("타임아웃(기본값 적용):", timeout)

# 4) dict 순회: 켜져 있는 기능만 골라내기
print("\n[활성화된 기능]")
for flag, on in config["feature_flags"].items():
    if on:                                 # True인 것만
        print(" -", flag)

# 5) 리스트 순회: enumerate로 번호 붙이기
print("\n[지점 목록]")
for i, region in enumerate(config["regions"], start=1):
    print(f" {i}. {region}")

# 6) 리스트 안의 dict 순회 + 조건으로 찾기
print("\n[관리자 목록]")
for admin in config["admins"]:
    print(f" {admin['name']:<6} {admin['role']:<8} {admin['email']}")
# <: 왼쪽 정렬;   >: 오른쪽 정렬,   ^: 가운데 정렬, 숫자: 출력 폭(width)
owners = [a["name"] for a in config["admins"] if a["role"] == "owner"]
print("소유자:", owners)

# 7) 값 수정하기 (dict/list는 그 자리에서 바뀜)
config["environment"] = "production"       # 값 덮어쓰기
config["database"]["use_ssl"] = True       # 중첩된 값 수정
config["feature_flags"]["enable_export_pdf"] = True
config["regions"].append("여의도점")        # 리스트에 추가
config["admins"].append({                  # 새 dict 추가
    "name": "박지호",
    "email": "jhpark@example.com",
    "role": "viewer",
})
config["notification"]["channels"].append("카카오톡")
config["updated_by"] = "class34.py"    # 새로운 키 추가

# 8) 저장: 파이썬 dict → JSON 파일
#    ensure_ascii=False → 한글이 \uXXXX 로 깨지지 않음
#    indent=2           → 사람이 읽기 좋게 들여쓰기
with open("config1_updated.json", "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)
print("\nconfig_updated.json 으로 저장했습니다.")

# 9) 검증: 저장한 파일을 다시 읽어서 의도대로 됐는지 확인
with open("config1_updated.json", "r", encoding="utf-8") as f:
    saved = json.load(f)
assert saved["environment"] == "production" # AssertionError 체크
assert saved["database"]["use_ssl"] is True
assert "여의도점" in saved["regions"]
assert len(saved["admins"]) == len(config["admins"])
assert "카카오톡" in saved["notification"]["channels"]
print("검증 통과!")