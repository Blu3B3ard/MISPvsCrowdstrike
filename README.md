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

JSON File Format and Information Needed:

    The JSON file (IOCs.json) should contain a list of IOCs in the following format:

    json

    [
        {
            "source": "MISP",
            "action": "detect",
            "expiration": "2023-01-22T15:00:00.000Z",
            "description": "IOC from MISP",
            "type": "<IOC_type>",
            "value": "<IOC_value>",
            "platforms": ["linux"],
            "severity": "LOW",
            "applied_globally": true
        },
        {
            "source": "MISP",
            "action": "detect",
            "expiration": "2023-01-22T15:00:00.000Z",
            "description": "IOC from MISP",
            "type": "<IOC_type>",
            "value": "<IOC_value>",
            "platforms": ["linux"],
            "severity": "LOW",
            "applied_globally": true
        }
    ]

        <IOC_type>: Type of the IOC (e.g., "ipv4", "domain", "hash").
        <IOC_value>: Value of the IOC (e.g., IP address, domain name, hash value).
        platforms: A list of platforms where the IOC is applicable (e.g., ["linux", "windows"]).
        severity: The severity level of the IOC (e.g., "LOW", "MEDIUM", "HIGH").
        applied_globally: A boolean indicating whether the IOC should be applied globally.

Important Notes

    Ensure that your MISP instance is properly configured and contains events tagged with "crowdstrike".
    Make sure that your CrowdStrike API credentials have the necessary permissions to create IOCs in the console.

Troubleshooting

    If you encounter any issues, ensure that all required libraries are installed and that your configuration variables are correctly set.
    Check the error messages provided by the script for guidance on troubleshooting.
