import json
from pymisp import ExpandedPyMISP
from falconpy import IOC

# MISP Configuration
MISP_URL = 'https://site.com'
MISP_KEY = '<your_api_key>'

# MISP conection
misp = ExpandedPyMISP(MISP_URL, MISP_KEY, True)

# Get the events in MISP with the TAG "crowdstrike"
events = misp.search(tags=['crowdstrike'])

# List all IOC's to save in a file
crowdstrike_iocs = []

# Format all MISP events
for event in events:
    for attribute in event['Event']['Attribute']:
        if 'value' in attribute:
            crowdstrike_iocs.append({
                "source": "MISP",
                "action": "detect",
                "expiration": "2023-01-22T15:00:00.000Z",
                "description": "IOC from MISP",
                "type": attribute['type'],
                "value": attribute['value'],
                "platforms": ["linux"],
                "severity": "LOW",
                "applied_globally": True
            })

# Write the IOC's in a .json file
with open('IOCs.json', 'w') as f:
    json.dump(crowdstrike_iocs, f)

# Define all credentials to Crowdstrike API
CLIENT_ID = '<your_client_id>'
CLIENT_SECRET = '<your_client_secret>'

# Connect to Crowdstrike API
falcon = IOC(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

# Read the IOC's.json file and send them to Crowdstrike console
try:
    with open('IOCs.json', 'r') as f:
        iocs = json.load(f)

    # Send each IOC to Crowdstrike Console
    for ioc in iocs:
        response = falcon.indicator_create_v1(
            action=ioc["action"],
            applied_globally=ioc["applied_globally"],
            description=ioc["description"],
            expiration=ioc["expiration"],
            platforms=ioc["platforms"],
            severity=ioc["severity"],
            source=ioc["source"],
            type=ioc["type"],
            value=ioc["value"]
        )
        print("IOC sent with success:", response)

except FileNotFoundError:
    print("The IOCs.json wasn't found.")
except json.JSONDecodeError:
    print("Error to decode the JSON file.")
except Exception as e:
    print("Error:", e)