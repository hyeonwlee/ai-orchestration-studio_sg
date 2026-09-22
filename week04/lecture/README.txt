AI 오케스트레이션 스튜디오 — 4주차 실습 자료 (buggy_scripts)
============================================================

[포함 파일]
- dirty_sales.csv   : 결측치·이상치·혼합 타입이 섞인 판매 데이터 500행
- buggy_1.py        : ValueError    (숫자 변환 실패)
- buggy_2.py        : KeyError      (컬럼명 문제)
- buggy_3.py        : AttributeError(None 전파)
- buggy_4.py        : 에러 없이 틀린 결과(결측치가 집계를 왜곡)
- buggy_5.py        : IndexError    (+ 이상치 혼재)

[사전 준비]
- 가상환경(.venv) 활성화 후:  pip install pandas openpyxl
- 다섯 스크립트와 dirty_sales.csv는 같은 폴더에 두고 실행한다.
  실행 예:  python buggy_1.py

[과제]
- 4주차 강의노트 '4. 4주차 과제'의 스크립트별 제출 형식(진단 3단계 루틴,
  수정 전후 코드 # FIXED 주석, 검증 증빙, usage_log.md)을 따른다.
- 각 스크립트 상단 주석에 진단 힌트가 있다. 코드를 실행해 Traceback을
  직접 얻는 것에서 시작하라.
