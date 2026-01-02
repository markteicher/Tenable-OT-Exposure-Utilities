# enums/plugin_hit_status.py
#
# Tenable OT Security – PluginHitStatus GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/pluginhitstatus.doc.html
#
# Purpose:
# - Represents the lifecycle status of a plugin hit

PLUGIN_HIT_STATUS_ENUM_NAME = "PluginHitStatus"

PLUGIN_HIT_STATUS_VALUES = [
    "Outstanding",
    "Mitigated",
    "Resurfaced",
]
