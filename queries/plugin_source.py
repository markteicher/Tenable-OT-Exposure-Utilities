# queries/plugin_source.py
#
# Tenable OT Security – PluginSource GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/pluginsource.doc.html
#
# Purpose:
# - Enumerates the origin/source of Plugin data

PLUGIN_SOURCE_ENUM_NAME = "PluginSource"

PLUGIN_SOURCES = [
    "Unknown",
    "NNM",
    "Nessus",
    "Tot",
]
