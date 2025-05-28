# 🔍 Web Vulnerability Auto-Scanner
자동으로 웹 페이지의 URL을 분석하고 SQL Injection 및 XSS 취약점을 탐지하는 경량화된 Python 기반 진단 도구입니다.

## 🎯 개요
- 대상: GET 파라미터 기반 동적 웹 페이지
- 기능: SQLi 및 XSS 취약점 탐지
- 결과: 콘솔 출력 + `report/result.txt` 로그 저장 + `report/report.html` html 보고서 출력


## 📁 디렉토리 구조

```bash
web_vuln_scanner/
├── main.py                          # 진단 실행 진입점
├── scanner/
│   ├──  __init__.py
│   ├── form_extractor.py             # HTML 폼 수집기
│   ├── payloads.py                   # 테스트 페이로드
│   ├── sql_injection_scanner.py      # SQLi 탐지
│   ├── xss_scanner.py                # XSS 탐지
│   └── report_generator.py           # HTML 리포트 생성
├── report/
│   ├── result.txt                  # 스캔 결과 저장
│   └── report.html                 # 시각적 HTML 보고서
└── README.md                       # 프로젝트 설명
```


## 🚀 실행 방법
```bash
python scanner.py --url "http://testphp.vulweb.com/listproducts.php?cat=1"
```


## 📌 ## 취약점 테스트 대상
- http://testphp.vulnweb.com
- DVWA (Damn Vulnerable Web Application)


## 🧠 탐지 기능
- SQLi : ' OR '1'='1 기반 에러 메시지 확인
- XSS : <script>alert(1)</script> 반사 여부 확인
  

## 🛠  향후 개선 아이디어
- POST 기반 스캔 기능 추가
- 쿠키 및 세션 설정 점검 기능 추가
- 보안 헤더 검사 기능 추가
- 명령어 인자(`argparse`) 기반 CLI 추가
- CSRF, Open Redirect 등 탐지 확장
- 탐지 결과 다양한 포맷으로 출력
- `robots.txt`, `sitemap.xml` 기반 자동 크롤링 확장
  

## 📄 자동 테스트용 스크립트
```python
http://testphp.vulnweb.com/listproductst.php?cat=1
http://testphp.vulnweb.com/artists.php?artist=1
```


## 👤 작성자
- 프로젝트 담당: 양예진
