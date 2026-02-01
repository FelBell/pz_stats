import time
import os
import json
import requests
import sys

LOG_FILE = os.environ.get('LOG_FILE_PATH', '/logs/server-console.txt')
API_URL = os.environ.get('API_URL', 'http://backend:5000/api/stats')

print(f"Starting Log Forwarder...", file=sys.stderr)
print(f"Watching {LOG_FILE}", file=sys.stderr)
print(f"Target API: {API_URL}", file=sys.stderr)

def follow(thefile):
    thefile.seek(0, 2) # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def main():
    # Wait for file to exist
    while not os.path.exists(LOG_FILE):
        print(f"Waiting for {LOG_FILE} to be created...", file=sys.stderr)
        time.sleep(5)

    with open(LOG_FILE, 'r') as f:
        loglines = follow(f)
        for line in loglines:
            # Look for our specific tag
            # Example log: "LOG  : General     , 1234567890> [PZ_STATS] {"event": "test"}"
            if "[PZ_STATS]" in line:
                try:
                    # Extract JSON part. Assuming everything after [PZ_STATS] is JSON
                    json_str = line.split("[PZ_STATS]", 1)[1].strip()
                    payload = json.loads(json_str)

                    print(f"Found stat: {payload}", file=sys.stderr)

                    # Send to Backend
                    try:
                        resp = requests.post(API_URL, json=payload, timeout=5)
                        if resp.status_code != 201:
                            print(f"Failed to send: {resp.status_code} - {resp.text}", file=sys.stderr)
                        else:
                            print("Sent successfully.", file=sys.stderr)
                    except requests.exceptions.RequestException as e:
                        print(f"Connection error to backend: {e}", file=sys.stderr)

                except json.JSONDecodeError:
                    print(f"Failed to parse JSON: {line}", file=sys.stderr)
                except Exception as e:
                    print(f"Error processing line: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()
