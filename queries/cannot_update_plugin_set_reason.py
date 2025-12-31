"""
queries/cannot_update_plugin_set_reason.py

Tenable OT Security – CannotUpdatePluginSetReason Enum

Source documentation:
https://docs.tenable.com/OT-security/api/cannotupdatepluginsetreason.doc.html

Purpose:
- Enumerates all reasons a Nessus plugin set update may be rejected
- Used for plugin update workflows, diagnostics, and failure analysis
- Enables deterministic handling of plugin update failures
"""

CANNOT_UPDATE_PLUGIN_SET_REASON = [
    "Unknown",
    "LicenseInactive",
    "EmLicenseInactive",
    "NessusNotReady",
    "OldLicense",
    "EmOldLicense",
    "UpdateAlreadyInProgress",
    "Unchanged",
    "NetworkError",
    "InvalidFile",
    "NoSpaceLeftOnDevice",
]
