# queries/plugin_severity.py
#
# Tenable OT Security – PluginSeverity GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/pluginseverity.doc.html
#
# Purpose:
# - Enumerates severity levels for Plugin-related queries

PLUGIN_SEVERITY_ENUM_NAME = "PluginSeverity"

PLUGIN_SEVERITY_LEVELS = [
    "Info",
    "Low",
    "Medium",
    "High",
    "Critical",
]
