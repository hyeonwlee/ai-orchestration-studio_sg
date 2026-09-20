## 3주차 AI 사용 기록
### 1. 활용한 AI 및 용도
- LLM(chatGPT) 사용
- pandas 메서드 확인
- 파이썬 파일 입출력 및 Excel 관련 개념 확인
- 작성한 코드 및 보고서 검증

###
---
---

### 2. 질문 및 답변 내용 정리
#### 2.1. pandas의 `.agg()` 메서드
- **질문 배경 및 입력 프롬프트**: 강의자료의 아래 코드를 보고, 그 동작 방식을 더욱 잘 이해하고자 하였다.
`report = df.groupby(["month", "category"])["sales"].agg(총매출="sum", 평균매출="mean", 거래건수="count")`
    > 입력 프롬프트: .agg() 가 무슨 메소드입니까

- **AI 답변 및 학습 내용**
    - `.agg()`는 aggregation(집계)을 위한 pandas 메서드이다.
    - 주로 `groupby()`와 함께 사용하여 그룹별로 하나 이상의 집계 함수를 적용할 수 있다.
    - 여러 집계 함수를 동시에 적용하거나 컬럼별로 서로 다른 집계 방법을 지정할 수 있다.

- **적용 내용**: 과제의 월별x카테고리별 매출 집계에 활용하였다.

---

#### 2.2. pandas의 `.reset_index()` 메서드
- **질문 배경 및 입력 프롬프트**: 강의자료의 다음 코드를 보고, 그 동작 방식을 더욱 잘 이해하고자 하였다.
`report = report.reset_index()`
    > 입력 프롬프트: .reset_index() 메서드는 어떤 기능이죠

- **AI 답변 및 학습 내용**
    - 현재 DataFrame의 인덱스를 일반적인 컬럼으로 변환하고, 새로운 기본 인덱스(0, 1, 2, ...)를 생성하는 메서드이다.
    - `groupby()` 결과에서는 그룹 기준이 인덱스로 들어가는 경우가 많기 때문에, 최종 결과를 일반적인 표 형태로 사용하기 위해 `reset_index()`를 자주 사용한다.
    - `reset_index(drop=True)`를 사용하면 기존 인덱스를 컬럼으로 보존하지 않고 삭제한 뒤 새로운 기본 인덱스를 생성한다.

- **적용 내용**: 과제의 월별x카테고리별 집계 결과와 카테고리별 합계 결과에서, 월과 카테고리를 일반 컬럼으로 사용하기 위해 활용하였다.

---

#### 2.3. 파이썬에서 Excel 파일을 읽는 방법
- **질문 배경 및 입력 프롬프트**
    > 입력 프롬프트:  
        from openpyxl import load_workbook  
        wb = load_workbook("inventory_sample.xlsx")   # 워크북(파일 전체)  
        print(wb.sheetnames)                          # 시트 이름 목록   
        ws = wb["재고현황"]                            # 워크시트 선택  
        print(ws["B2"].value)                         # 셀 단위 접근  
        for row in ws.iter_rows(min_row=2, values_only=True):  
            print(row)                                # 튜플로 행 순회  
        이건 뭡니까. 파이썬에서 엑셀 파일을 읽는 방법이 여러가지인가요. 

- **AI 답변 및 학습 내용**
    - `openpyxl`은 Excel 파일을 직접 다루기 위한 파이썬 라이브러리이다. Workbook, Worksheet, Cell 방식으로 .xlsx 파일의 구조 자체에 접근할 수 있다. 특정 셀의 값이나 시트, 서식 등을 직접 확인하거나 수정할 때 유용하다.
    - 한편 `pandas.read_excel()`은 Excel의 표 데이터를 pandas의 DataFrame으로 불러오는 방법이다. Excel 데이터를 분석하거나 groupby(), agg() 등의 pandas 기능을 활용할 때 적합하다.

- **적용 내용**: 이번 과제에서는 CSV 데이터를 pandas DataFrame으로 불러와 분석하고, ExcelWriter를 이용하여 집계 결과를 Excel 파일로 저장하였다. 저장된 Excel 파일의 결과를 확인하기 위해서는 read_excel()을 사용하였다.

---

#### 2.4. 파일 접근 권한 오류
- **질문 배경 및 입력 프롬프트**: pipeline.py 실행하였을 때 아래와 같은 오류가 확인되어, 원인을 정확히 파악하고자 질문하였다.
    > 입력 프롬프트:  
        Traceback (most recent call last):  
        (~ 오류 내용 ~)  
        PermissionError: [Errno 13] Permission denied: 'Monthly_Report.xlsx'  
        이건 무슨 오류일까요.

- **AI 답변 및 학습 내용**
    - PermissionError: [Errno 13]은 파일에 접근하거나 쓰는 과정에서 권한이 거부되었음을 의미한다.
    - pd.ExcelWriter()를 이용하여 기존 Excel 파일에 쓰려고 할 때 해당 파일이 Excel 등 다른 프로그램에서 열려 있으면 Windows가 파일을 잠그기 때문에 이러한 오류가 발생할 수 있다.

- **해결**: Excel에서 열려있는 Monthly_Report.xlsx 파일을 닫은 후 다시 실행하여 정상적으로 동작하는 것을 확인하였다.

###
---
---

### 3. 작성한 코드 검토 및 수정 내역
> 입력 프롬프트:  
        (~ 과제 요구사항 ~)  
        (~ 기존에 작성했던 코드 ~)  
        해당 과제에 대한 제출 코드로 어떻습니까? 개선 사항 있다면 말씀해 주십시오.

#### 3.1. 카테고리별합계 집계 결과를 별도 변수로 분리
- **기존 코드**: 집계부터 Excel 저장까지 한 줄로 작성하였었다.  
    ```python
    df.groupby("카테고리")["매출액"].sum().reset_index().sort_values("매출액", ascending=False).to_excel(...)
    ```

- **AI의 제안**: 코드의 가독성을 위해 중간 결과를 `category_report` 변수에 저장하기를 권장하였다.  
    ```python
    category_report = df.groupby("카테고리")["매출액"].sum().reset_index().sort_values("매출액", ascending=False)

    category_report.to_excel(writer, sheet_name="카테고리별합계", index=False)
    ```

- **채택 여부**: 제안 내용을 채택하여 코드의 가독성을 높였다.

---

#### 3.2. 거래건수 집계 방식 검토
- **기존 코드**: 거래건수를 세는 데 count()를 사용하였다.  
    `.agg(총매출="sum", 평균매출="mean", 거래건수="count")`

- **AI의 제안**: 별도의 결측치 여부와 관계없이 실제 거래 건수를 세는 목적이라면 size()가 의미상 더 명확하다. count()는 집계 대상 컬럼에서 결측치가 아닌 값의 개수를 세고, size()는 해당 그룹의 행 개수를 세기 때문이다.

- **채택 여부**: 이번 과제의 데이터에서는 매출액에 결측치가 없어 count()와 size()의 결과가 동일하였다. 따라서 기존 코드를 유지하였다.

###
---
---

### 4. 보고서 개선
- 보고서 다듬어 달라고 요청하였다.
- 문장의 어색한 표현을 수정하고, 항목별 내용을 구분하여 가독성을 높이는 방향으로 일부 내용을 수정하였다.