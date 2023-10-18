import requests
import random

# 1. TARGET SPECIFICATION
TARGET_URL = input("Enter the website, e.g http://example.com/login : ")

# 2. PAYLOAD LIBRARY
def load_payloads(filename):
    with open(filename, 'r') as file:
        payloads = [line.strip() for line in file.readlines()]
    return payloads

PAYLOADS = load_payloads('payloads.txt')

HEADERS = {
    "User-Agent": "SQLiScanner/1.0",  # This will be replaced with a random user-agent
    "Accept-Language": "en-US,en;q=0.5",  # Default language preference
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "DNT": "1",  # Do not track request header
    # Add more headers if necessary, e.g., authentication headers, cookies
}

USER_AGENTS = [
    "SQLiScanner/1.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Mozilla/5.0 (X11; U; Linux x86_64; hu-HU) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4"
    # Add more user-agents...
]

# 3. SCANNER ENGINE
def send_payload(url, payload):
    data = {
        "user": payload,  # Adjust parameter names based on your application
        "pass": "dummy_password",
    }
    HEADERS["User-Agent"] = random.choice(USER_AGENTS)  # Set a random user-agent
    try:
        response = requests.post(url, data=data, headers=HEADERS, timeout=30)
    except requests.RequestException as e:
        print(f"Error sending payload: {payload}. Error: {e}")

        return None

# 4. RESULT ANALYZER
def analyze_response(response):
    error_messages = [
        "database error",
        "mysql_fetch",
        "SQL syntax",
        # ... add more error indicators as needed
    ]
    for error in error_messages:
        if error in response.text:
            return True
    return False

# MAIN SCANNER LOGIC
def main():
    vulnerable = False
    for payload in PAYLOADS:
        print(f"Testing payload: {payload}")
        response = send_payload(TARGET_URL, payload)
        if response and analyze_response(response):
            print(f"[VULNERABLE] Detected SQLi vulnerability with payload: {payload}")
            with open("vulnerability_log.txt", "a") as log:
                log.write(f"[VULNERABLE] Detected SQLi vulnerability with payload: {payload}\n")
            vulnerable = True
            break

    if not vulnerable:
        print("No vulnerabilities detected.")
        with open("vulnerability_log.txt", "a") as log:
            log.write("No vulnerabilities detected.\n")

if __name__ == "__main__":
    main()
