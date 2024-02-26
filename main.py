import requests
import csv

# Replace these variables with your actual data
API_KEY = 'your_meraki_api_key'
ORGANIZATION_ID = 'your_organization_id'
# Path to your CSV.  If it is in the same directory as the script, just use the filename
CSV_FILE_PATH = 'path_to_your_csv_file.csv'

# Endpoint URL
url = f'https://api.meraki.com/api/v1/organizations/{ORGANIZATION_ID}/inventory/claim'

# Headers
headers = {
    'X-Cisco-Meraki-API-Key': API_KEY,
    'Content-Type': 'application/json'
}

# Function to read license keys from a CSV file
def read_license_keys_from_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        return [row[0] for row in reader]  # Assumes each row contains one license key

# Read license keys from CSV
LICENSE_KEYS = read_license_keys_from_csv(CSV_FILE_PATH)

# Data payload
data = {
    'licenses': [{'key': key} for key in LICENSE_KEYS],
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

# Check response status
if response.status_code == 200:
    print("Licenses successfully claimed into the organization inventory.")
else:
    print("Failed to claim licenses. Status code:", response.status_code)
    print("Response:", response.text)
