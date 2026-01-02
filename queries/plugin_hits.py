# queries/plugin_hits.py
#
# Tenable OT Security – PluginHits GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/pluginhits.doc.html
#
# Purpose:
# - Enumerates fields for Plugin hit records (asset-level plugin detections)

PLUGIN_HITS_ENUM_NAME = "pluginHits"

PLUGIN_HITS_FIELDS = [
    "assetId",
    "pluginId",
    "port",
    "protocol",
    "svcName",
    "time",
    "mitigatedAt",
    "mitigationDuration",
    "output",
    "status",
    "severity",
]
