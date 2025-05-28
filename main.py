import os
from scanner.sql_injection_scanner import scan_sql_injection
from scanner.xss_scanner import scan_xss
from scanner.report_generator import generate_html_report

def save_results_to_txt(sql_results, xss_results, path="report/result.txt"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("=== SQL Injection Vulnerabilities ===\n")
        if not sql_results:
            f.write("No SQLi vulnerabilities found.\n")
        else:
            for form, payload in sql_results:
                f.write(f"Form action: {form['action']}\nPayload: {payload}\n\n")

        f.write("\n=== XSS Vulnerabilities ===\n")
        if not xss_results:
            f.write("No XSS vulnerabilities found.\n")
        else:
            for form, payload in xss_results:
                f.write(f"Form action: {form['action']}\nPayload: {payload}\n\n")

def main():
    target_url = input("Enter target URL: ").strip()

    print("\n[+] Scanning for SQL Injection...")
    sql_results = scan_sql_injection(target_url)

    print("[+] Scanning for XSS...")
    xss_results = scan_xss(target_url)

    print("\n[+] Saving results to report/result.txt...")
    save_results_to_txt(sql_results, xss_results, path="report/result.txt")

    print("[+] Generating HTML report to report/report.html...")
    generate_html_report(sql_results, xss_results, output_path="report/report.html")

    print("\n[✓] Done. Check report/result.txt and report/report.html.")

if __name__ == "__main__":
    main()
