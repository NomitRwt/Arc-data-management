import requests
from datetime import datetime

# Enter the username, password, portal url
username = "username"
password = "password"
portal_url = "portal_url"

# URLs of individual services (add more if needed)
SERVICES_TO_CHECK = [
    "https://your-server.domain.com/arcgis/rest/services/Folder1/ServiceA/MapServer",
    "https://your-server.domain.com/arcgis/rest/services/Folder1/ServiceB/FeatureServer",
    "https://your-server.domain.com/arcgis/rest/services/ServiceC/MapServer"
]

# Optional Token (leave as None if not needed)
TOKEN = generater_token(username, password, portal_url)  # Replace with actual token or call a function to get it

# Log file location
LOG_FILE = "C:/Logs/arcgis_individual_services_status_log.txt"

def generate_token(username, password, portal_url):
    url = f"{portal_url}/sharing/rest/generateToken"
    data = {
        "username": username,
        "password": password,
        "client": "referer",
        "referer": portal_url,
        "expiration": 60,
        "f": "json"
    }
    response = requests.post(url, data=data)
    return response.json().get("token")

def check_service(url, token=None):
    try:
        params = {}
        if token:
            params['token'] = token
            params['f'] = 'json'

        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            return "UP"
        else:
            return f"DOWN ({response.status_code})"
    except requests.exceptions.RequestException as e:
        return f"DOWN ({str(e)})"

def main():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_lines = [f"{timestamp} - Checking ArcGIS Services..."]

    for service_url in SERVICES_TO_CHECK:
        status = check_service(service_url, token=TOKEN)
        log_lines.append(f"{service_url} => {status}")

    log_output = "\n".join(log_lines)
    print(log_output)

    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_output + "\n\n")

if __name__ == "__main__":
    main()
