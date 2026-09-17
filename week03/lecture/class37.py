# 인코딩을 모르는 파일을 안전하게 읽는 관용 패턴
def read_text_safely(path):
    for enc in ("utf-8", "cp949"):
        try:
            with open(path, "r", encoding=enc) as f:
                return f.read(), enc
        except UnicodeDecodeError:
            continue
    raise ValueError(f"지원하지 않는 인코딩: {path}")

text, used = read_text_safely("legacy_sales.csv")
print(f"성공한 인코딩: {used}")
