# MISPvsCrowdstrike
MISP to CrowdStrike IOC Sender

This script allows you to extract IOCs (Indicators of Compromise) tagged with "crowdstrike" from MISP (Malware Information Sharing Platform) and send them to the CrowdStrike console.
Requirements

    Python 3.x
    pymisp library: Installation instructions can be found here.
    falconpy library: Installation instructions can be found here.

Usage

    Install the required libraries using pip:

    bash

pip install pymisp falconpy

Configure the script:

    Set up your MISP instance URL and API key in the MISP_URL and MISP_KEY variables, respectively.
    Set up your CrowdStrike API credentials in the CLIENT_ID and CLIENT_SECRET variables.

Run the script:

bash

    python misp_to_crowdstrike_ioc_sender.py

Script Explanation

    The script connects to your MISP instance using the pymisp library and searches for events tagged with "crowdstrike".
    It then extracts IOCs (Indicators of Compromise) from these events and saves them to a JSON file named IOCs.json.
    Next, it connects to the CrowdStrike API using the falconpy library and sends the IOCs to the CrowdStrike console.

Important Notes

    Ensure that your MISP instance is properly configured and contains events tagged with "crowdstrike".
    Make sure that your CrowdStrike API credentials have the necessary permissions to create IOCs in the console.

Troubleshooting

    If you encounter any issues, ensure that all required libraries are installed and that your configuration variables are correctly set.
    Check the error messages provided by the script for guidance on troubleshooting.
