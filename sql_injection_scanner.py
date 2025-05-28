import requests

from urllib.parse import urlparse, parse_qs, urlencode

SQLI_PAYLOADS = ["'", "' OR '1'='1", "' OR 1=1--", "';--", "\" OR \"1\"=\"1"]

def test_sqli(url):
    print("[*] SQL Injection 테스트 중...")
    parsed = urlparse(url)
    base = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    params = parse_qs(parsed.query)

    vulnerable = False

    for param in params:
        original_value = params[param][0]
        for payload in SQLI_PAYLOADS:
            temp_params = params.copy()
            temp_params[param] = original_value + payload
            test_url = f"{base}?{urlencode(temp_params, doseq=True)}"
            try:
                res = requests.get(test_url, timeout=5)
                if any(error in res.text.lower() for error in ["sql syntax", "mysql", "warning", "error"]):
                    print(f"[!] SQLi 취약점 발견: {test_url}")
                    log_result("SQLi", test_url)
                    vulnerable = True
                    break
            except Exception as e:
                print(f"[-] 요청 실패: {e}")

    if not vulnerable:
        print("[-] SQLi 취약점 발견되지 않음.")

def log_result(vuln_type, url):
    with open("report/result.txt", "a", encoding="utf-8") as f:
        f.write(f"[{vuln_type}] {url}\n")


import requests
from .payloads import sql_payloads
from .form_extractor import get_forms, get_form_details

def is_sql_error(response_text):
    errors = ["you have an error in your sql syntax", "warning: mysql", "unclosed quotation", "sqlite error"]
    return any(error in response_text.lower() for error in errors)

def scan_sql_injection(url):
    forms = get_forms(url)
    vulnerable = []
    for form in forms:
        form_details = get_form_details(form, url)
        for payload in sql_payloads:
            data = {}
            for input in form_details['inputs']:
                if input['type'] != 'submit' and input['name']:
                    data[input['name']] = payload
            if form_details['method'] == 'post':
                res = requests.post(form_details['action'], data=data)
            else:
                res = requests.get(form_details['action'], params=data)
            if is_sql_error(res.text):
                vulnerable.append((form_details, payload))
                break
    return vulnerable

