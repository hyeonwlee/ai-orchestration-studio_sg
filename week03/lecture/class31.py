# 쓰기: 파일이 없으면 생성, 있으면 내용을 덮어쓴다(mode="w")
with open("memo.txt", "w", encoding="utf-8") as f:
    f.write("1행: 데이터 핸들링 시작\n")
    f.write("2행: with 구문은 자동으로 닫아 준다\n")

# 읽기(mode="r")
with open("memo.txt", "r", encoding="utf-8") as f:
    content = f.read()          # 전체를 문자열 하나로
print(content)

# 한 줄씩 순회하며 읽기 (대용량 파일에 유리)
with open("memo.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())     # strip(): 양끝 공백/개행 제거
