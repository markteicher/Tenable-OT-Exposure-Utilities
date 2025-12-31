"""
queries/capability.py

Tenable OT Security – Capability GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/capability.doc.html

Purpose:
- Enumerate all permissions (capabilities) supported by Tenable OT
- Used for roles, authorization checks, and access control
"""

CAPABILITY_ENUM_NAME = "Capability"

CAPABILITIES = [
    "ReadEvents",
    "WriteEvents",
    "ResolveEvents",
    "ReadPolicies",
    "WritePolicies",
    "ReadAssets",
    "WriteAssets",
    "AssetQueries",
    "PortScan",
    "ReadVulnerabilities",
    "WriteVulnerabilities",
    "ReadNetwork",
    "WriteNetwork",
    "ToggleCapture",
    "ReadGroups",
    "WriteGroups",
    "DeviceSettings",
    "WriteOverlappingIps",
    "ReadOverlappingIps",
    "ReadCredentials",
    "WriteCredentials",
    "CustomFieldsSettings",
    "AcmSettings",
    "ApiKeys",
    "HttpsSettings",
    "QueriesSettings",
    "ReadServers",
    "WriteServers",
    "Integrations",
    "SystemSettings",
    "PcapPlayer",
    "FactoryReset",
    "DeleteAssets",
    "ReadSensors",
    "WriteSensors",
    "NessusUserScan",
    "ReadUpdates",
    "WriteUpdates",
    "ReadActiveQueries",
    "WriteActiveQueries",
    "ForceActiveQueries",
    "WritePairing",
    "ReadPairing",
    "WriteEmIcps",
    "ReadEmIcps",
    "IotConnectors",
    "PcapDownload",
    "UpdateIcp",
    "ReadOtAgents",
    "WriteOtAgents",
    "UserGroups",
    "Users",
    "Zones",
    "AuthServers",
    "Roles",
    "UserInfo",
]
