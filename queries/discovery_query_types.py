"""
queries/discovery_query_types.py

Tenable OT Security – DiscoveryQueryTypes GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/discoveryquerytypes.doc.html

Purpose:
- Enumerates supported discovery query types
"""

DISCOVERY_QUERY_TYPES_ENUM_NAME = "DiscoveryQueryTypes"

DISCOVERY_QUERY_TYPES = [
    "IcsDiscovery",
    "AssetDiscoveryType",
    "DnsType",
    "PortScanQueryType",
    "PortScanAssetEnrichment",
    "InactiveAssetProbe",
    "SubnetsDiscovery",
]
