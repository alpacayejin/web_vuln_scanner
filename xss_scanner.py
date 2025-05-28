import requests
from .payloads import xss_payloads
from .form_extractor import get_forms, get_form_details

def scan_xss(url):
    forms = get_forms(url)
    vulnerable = []
    for form in forms:
        form_details = get_form_details(form, url)
        for payload in xss_payloads:
            data = {}
            for input in form_details['inputs']:
                if input['type'] != 'submit' and input['name']:
                    data[input['name']] = payload
            if form_details['method'] == 'post':
                res = requests.post(form_details['action'], data=data)
            else:
                res = requests.get(form_details['action'], params=data)
            if payload in res.text:
                vulnerable.append((form_details, payload))
                break
    return vulnerable
