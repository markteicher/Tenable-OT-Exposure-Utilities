"""
queries/ot_agent_select_field.py

Tenable OT Security – OtAgentSelectField GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/otagentselectfield.doc.html

Purpose:
- Enumerates selectable fields for OT Agent queries
"""

OT_AGENT_SELECT_FIELD_ENUM_NAME = "OtAgentSelectField"

OT_AGENT_SELECT_FIELDS = [
    "id",
    "name",
    "version",
    "scannerVersion",
    "host",
    "status",
    "statusTs",
    "hostAsset",
    "hostAssetName",
    "hostAssetType",
    "lastScanStartTime",
    "lastScanEndTime",
    "lastScanResult",
    "hostOs",
    "schedule",
    "scheduleEnabled",
    "networks",
    "credentials",
    "assets",
    "lastScanDuration",
    "scanDuplicatedNetworks",
    "scoutRunStatus",
    "agentUpdateAvailable",
    "scoutUpdateAvailable",
    "createdTs",
    "origin",
    "shortVersion",
    "shortScannerVersion",
]
