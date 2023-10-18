# SQL Injection Vulnerability Scanner

## Overview

This project is an educational demonstration of a basic automated SQL injection vulnerability scanner. Designed to test web applications for potential SQL injection vulnerabilities, it automates the detection process by sending a list of common malicious payloads. SQL injection is a prevalent security flaw where attackers can inject malicious SQL code into queries. This tool illustrates how automated scanning can be performed and should only be used on environments with explicit permission.

## Features

- **Payload Loading**: Efficiently retrieves payloads from a `.txt` file containing common SQL attack patterns.
- **Automated Testing**: Transmits each payload to the specified target URL.
- **Response Analysis**: Assesses potential vulnerabilities using specific error indicators.
- **User Interaction**: Offers a straightforward CLI for users to initiate the vulnerability scan.

## Important Note

This tool uses a list of widespread SQL injection payloads. Websites equipped with a half-decent Web Application Firewall (WAF) will likely detect and block many of these attempts. While the objective is not to evade high-level security defenses, it serves to demonstrate a foundational scanning method.

## Usage

1. **Setup**
   - Update the `TARGET_URL` in the script to direct to a site you're authorized to test.
   - Confirm the `payloads.txt` file is in the same directory or provide its full path.

2. **Scanning**
   - Execute the script.
   - The scanner will evaluate each payload and highlight potential weak points.

## Code Structure

- `load_payloads(filename)`: Extracts payloads from the `.txt` file, returning a list.
- `send_payload(url, payload)`: Delivers the payload to the target URL.
- `analyze_response(response)`: Inspects the server's feedback for signs of an SQLi vulnerability.
- `main()`: Orchestrates the payload loading, sending, and analyzing phases.

## What I Learned

### Web Security Concepts
- **SQL Injection**: Delved deeper into the mechanisms by which malevolent SQL code can exploit unsecured application logic.
- **Server Responses**: Recognized how server feedback patterns can expose weaknesses.
- **Ethical Testing**: Re-emphasized the crucial nature of securing permissions prior to vulnerability assessments.

### Python Programming
- **Requests Library**: Utilized the library to manage HTTP transmissions.
- **File Handling**: Mastered reading and organizing payloads from an external source.
- **Error Handling**: Crafted solutions to gracefully manage unforeseen server feedback and other potential issues.

## Future Improvements

- **Expanded Payload List**: Broaden the spectrum of payloads to detect less common SQL attacks.
- **Response Time Analysis**: Integrate evaluations for Blind SQL Injection based on server response times.
- **Proxy Support**: Augment the capability to send requests via proxies, enhancing anonymity.
- **Rate Limiting**: Add intervals between transmissions to circumvent rate limitations and security alerts.

## Getting Started

Ensure Python and the `requests` library are installed. Start the scanner using:

```bash
python injector.py
```