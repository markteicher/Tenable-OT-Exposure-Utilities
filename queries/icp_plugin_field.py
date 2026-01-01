"""
queries/icp_plugin_field.py

Tenable OT Security – IcpPluginField GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/icppluginfield.doc.html

Purpose:
- Enumerates fields available for ICP plugin queries
"""

ICP_PLUGIN_FIELD_ENUM_NAME = "IcpPluginField"

ICP_PLUGIN_FIELDS = [
    "id",
    "name",
    "severity",
    "family",
    "vprScore",
    "modificationDate",
    "affectedAssets",
    "site",
]
