# Meraki License Claimer
This Python script automates the process of claiming license keys into an organization's inventory using the Cisco Meraki API. It's designed to streamline the management of licenses by reading them from a CSV file and claiming them in bulk.

## Prerequisites
Python 3.x
requests library (Install using pip install requests)<br>
A valid Cisco Meraki API Key<br>
The Organization ID where licenses need to be claimed<br>
A CSV file containing the license keys (one per line, no header)<br>
## Installation
Clone this repository to your local machine.<br>
Ensure Python 3.x is installed on your system.<br>
Install the requests library if not already installed:<br>

`
        sh  
        pip install requests  
`

## Configuration
Before running the script, you need to set up a few things:<br>

API Key: Open the script and locate the API_KEY variable. Replace 'your_meraki_api_key' with your actual Cisco Meraki API Key.<br>
Organization ID: Replace 'your_organization_id' in the ORGANIZATION_ID variable with the ID of the organization where you wish to claim the licenses.<br>
CSV File Path: Update the CSV_FILE_PATH variable with the path to your CSV file containing the license keys.<br>
<br>
No headers or additional columns are needed.<br>

## Usage
With the configuration set, you're ready to claim licenses. Run the script from your terminal:<br>

`
        sh  
        main.py  
`

The script will read each license key from the CSV file and attempt to claim them into the specified organization's inventory. Success or failure messages will be printed to the console for each license key.<br>

## Troubleshooting
API Key or Organization ID Errors: Ensure your API Key and Organization ID are correctly entered and that your API key has the necessary permissions.<br>
CSV Format Issues: Verify that the CSV file is properly formatted with one license key per line, and there are no headers or extra spaces.<br>
## Support
For questions or issues, please open an issue on GitHub.

## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.<br>

Please ensure to update tests as appropriate.

## License
https://github.com/CiscoSE/cisco-sample-code/blob/master/LICENSE