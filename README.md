# Meraki License Claimer
This Python script automates the process of claiming license keys into an organization's inventory using the Cisco Meraki API. It's designed to streamline the management of licenses by reading them from a CSV file and claiming them in bulk.

## Prerequisites
Python 3.x
requests library (Install using pip install requests)
A valid Cisco Meraki API Key
The Organization ID where licenses need to be claimed
A CSV file containing the license keys (one per line, no header)
## Installation
Clone this repository to your local machine.
Ensure Python 3.x is installed on your system.
Install the requests library if not already installed:
sh
Copy code
`
pip install requests
`
## Configuration
Before running the script, you need to set up a few things:

API Key: Open the script and locate the API_KEY variable. Replace 'your_meraki_api_key' with your actual Cisco Meraki API Key.
Organization ID: Replace 'your_organization_id' in the ORGANIZATION_ID variable with the ID of the organization where you wish to claim the licenses.
CSV File Path: Update the CSV_FILE_PATH variable with the path to your CSV file containing the license keys.

No headers or additional columns are needed.

## Usage
With the configuration set, you're ready to claim licenses. Run the script from your terminal:

sh
Copy code
`
python meraki_license_claim.py
`
The script will read each license key from the CSV file and attempt to claim them into the specified organization's inventory. Success or failure messages will be printed to the console for each license key.

## Troubleshooting
API Key or Organization ID Errors: Ensure your API Key and Organization ID are correctly entered and that your API key has the necessary permissions.
CSV Format Issues: Verify that the CSV file is properly formatted with one license key per line, and there are no headers or extra spaces.
## Support
For questions or issues, please open an issue on GitHub.

## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please ensure to update tests as appropriate.

## License
https://github.com/CiscoSE/cisco-sample-code/blob/master/LICENSE