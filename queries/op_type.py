"""
queries/op_type.py

Tenable OT Security – OpType GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/optype.doc.html

Purpose:
- Enumerates operation/query types used by ActiveQuery and related objects
"""

OP_TYPE_ENUM_NAME = "OpType"

OP_TYPES = [
    "Unknown",
    "CharacteristicsType",
    "RunStatusType",
    "SnapshotType",
    "SnmpType",
    "NbstatQueryType",
    "IdentificationType",
    "PortScanQueryType",
    "PortScanAssetEnrichment",
    "WmiType",
    "DnsType",
    "ArpType",
    "WmiUsbType",
    "AssetDiscoveryType",
    "BpScanType",
    "NessusBasicScanType",
    "IcsDiscovery",
    "InactiveAssetProbe",
    "PingType",
    "SubnetsDiscovery",
]
