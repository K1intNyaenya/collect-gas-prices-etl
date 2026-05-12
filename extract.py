import http.client
import json
from pathlib import Path

def extract():
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey API_KEY"
    }

    conn.request("GET", "/gasPrice/stateUsaPrice?state=WA", headers=headers)

    res = conn.getresponse()
    data = res.read()

    parsed_data = json.loads(data.decode("utf-8"))

    # current project directory
    project_root = Path(__file__).resolve().parent

    file_path = project_root / "gas_prices.json"

    with open(file_path, "w") as f:
        json.dump(parsed_data, f, indent=4)

    print(f"Saved to: {file_path}")

if __name__ == "__main__":
    extract()