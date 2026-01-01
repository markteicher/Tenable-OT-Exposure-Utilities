"""
queries/it_query_types.py

Tenable OT Security – ItQueryTypes GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/itquerytypes.doc.html

Purpose:
- Enumerates supported IT query types used by Tenable OT discovery and scanning
"""

IT_QUERY_TYPES_ENUM_NAME = "ItQueryTypes"

IT_QUERY_TYPES = [
    "ArpType",
    "NbstatQueryType",
    "SnmpType",
    "WmiType",
    "WmiUsbType",
    "NessusBasicScanType",
]
