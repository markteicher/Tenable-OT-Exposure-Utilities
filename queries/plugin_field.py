# queries/plugin_field.py
#
# Tenable OT Security – PluginField GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/pluginfield.doc.html
#
# Purpose:
# - Enumerates selectable fields for Plugin queries

PLUGIN_FIELD_ENUM_NAME = "PluginField"

PLUGIN_FIELDS = [
    "id",
    "source",
    "family",
    "name",
    "severity",
    "vprScore",
    "vprLevel",
    "affectedAssets",
    "fixedAssets",
    "modificationDate",
    "comment",
    "owner",
    "cvss3Score",
]
