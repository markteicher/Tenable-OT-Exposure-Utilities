"""
queries/mapping_rate.py

Tenable OT Security – MappingRate GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/mappingrate.doc.html

Purpose:
- Enumerates possible port mapping scan rates
"""

MAPPING_RATE_ENUM_NAME = "MappingRate"

MAPPING_RATES = [
    "OnePort",
    "TwoPorts",
    "FivePorts",
    "TenPorts",
    "FiftyPorts",
    "HundredPorts",
    "FiveHundredPorts",
    "ThousandPorts",
]
