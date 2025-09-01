# scanners.py
import requests
from urllib.parse import urljoin
from utils.logger import log_result

# Load payloads from files
def load_payloads(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

SQLI_PAYLOADS = load_payloads("payloads/sqli_payloads.txt")
XSS_PAYLOADS = load_payloads("payloads/xss_payloads.txt")

def test_sqli(url):
    """Test URL parameters for SQL Injection"""
    if "?" not in url:
        return
    for payload in SQLI_PAYLOADS:
        test_url = url + payload
        try:
            res = requests.get(test_url, timeout=5)
            if "error" in res.text.lower() or "sql" in res.text.lower():
                log_result(test_url, "SQLi")
        except requests.RequestException:
            continue

def test_xss(url):
    """Test forms for XSS"""
    from utils.crawler import get_forms
    forms = get_forms(url)
    for form in forms:
        action = form.get("action")
        post_url = urljoin(url, action)
        inputs = form.find_all("input")
        data = {}
        for input_tag in inputs:
            name = input_tag.get("name")
            if name:
                data[name] = XSS_PAYLOADS[0]
        try:
            res = requests.post(post_url, data=data, timeout=5)
            if XSS_PAYLOADS[0] in res.text:
                log_result(post_url, "XSS")
        except requests.RequestException:
            continue
