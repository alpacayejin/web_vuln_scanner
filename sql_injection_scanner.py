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
