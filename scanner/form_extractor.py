from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def get_forms(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    return soup.find_all("form")

def get_form_details(form, url):
    details = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details['action'] = urljoin(url, action)
    details['method'] = method
    details['inputs'] = inputs
    return details
