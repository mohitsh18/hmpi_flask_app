import requests
import json

# Sample data for testing
test_data = {
    "heavyMetalConcentrations": {
        "lead": 0.02,
        "cadmium": 0.004,
        "arsenic": 0.015,
        "mercury": 0.002,
        "chromium": 0.04
    },
    "latitude": 37.7749,
    "longitude": -122.4194
}

# Send POST request to the API
url = "http://localhost:3001/api/hmpi/calculate"
headers = {"Content-Type": "application/json"}
response = requests.post(url, data=json.dumps(test_data), headers=headers)

# Print the results
if response.status_code == 200:
    result = response.json()
    print("HMPI Calculation Results:")
    print(f"HPI: {result['HPI']:.2f}")
    print(f"HEI: {result['HEI']:.2f}")
    print(f"MI: {result['MI']:.2f}")
    print(f"Cd: {result['Cd']:.2f}")
    print(f"Nemerow: {result['Nemerow']:.2f}")
    print(f"Classification: {result['classification']}")
    if 'latitude' in result:
        print(f"Latitude: {result['latitude']}")
    if 'longitude' in result:
        print(f"Longitude: {result['longitude']}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
