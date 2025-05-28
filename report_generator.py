def generate_html_report(sql_results, xss_results, output_path="report.html"):
    html = """
    <html>
    <head><title>Vulnerability Scan Report</title></head>
    <body>
    <h1>Web Vulnerability Scan Report</h1>
    """

    html += "<h2>SQL Injection Results</h2>"
    if not sql_results:
        html += "<p>No SQL Injection vulnerabilities found.</p>"
    else:
        for form, payload in sql_results:
            html += f"<div><b>Form Action:</b> {form['action']}<br><b>Payload:</b> {payload}</div><hr>"

    html += "<h2>XSS Results</h2>"
    if not xss_results:
        html += "<p>No XSS vulnerabilities found.</p>"
    else:
        for form, payload in xss_results:
            html += f"<div><b>Form Action:</b> {form['action']}<br><b>Payload:</b> {payload}</div><hr>"

    html += "</body></html>"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
