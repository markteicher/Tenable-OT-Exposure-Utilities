"""
queries/firewall_op_type.py

Tenable OT Security – FirewallOpType GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/firewalloptype.doc.html

Purpose:
- Enumerates operations that can be blocked with a firewall rule
"""

FIREWALL_OP_TYPE_ENUM_NAME = "FirewallOpType"

FIREWALL_OP_TYPES = [
    "CharacteristicsType",
    "RunStatusType",
    "SnapshotType",
    "SnmpType",
    "NbstatQueryType",
    "IdentificationType",
    "PortScanQueryType",
    "PortScanAssetEnrichment",
    "WmiType",
    "WmiUsbType",
    "AssetDiscoveryType",
    "BpScanType",
    "NessusBasicScanType",
    "IcsDiscovery",
    "InactiveAssetProbe",
    "PingType",
    "SubnetsDiscovery",
]
