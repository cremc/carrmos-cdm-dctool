import requests
import sys

# Try 127.0.0.1 instead of localhost
BASE_URL = "http://127.0.0.1:8000"

def check_endpoint(endpoint):
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.get(url, timeout=5)
        print(f"GET {url} -> {response.status_code}")
        if response.status_code != 200:
            print(f"Error content: {response.text[:200]}")
    except requests.exceptions.RequestException as e:
        print(f"GET {url} -> FAILED: {e}")

def main():
    print(f"Checking API at {BASE_URL}...")
    try:
        # Increase timeout
        requests.get(f"{BASE_URL}/docs", timeout=5)
        print("Server is reachable.")
    except Exception as e:
        print(f"Server is NOT reachable at {BASE_URL}. Error: {e}")
        return

    endpoints = [
        "/academics/academic_levels/",
        "/academics/discipline_groups/",
        "/academics/disciplines/",
        "/general/countries/",
        "/general/provinces/",
        "/finance/currencies/",
        "/institution/categories/",
        "/institution/institutions/"
    ]

    for ep in endpoints:
        check_endpoint(ep)

if __name__ == "__main__":
    main()
