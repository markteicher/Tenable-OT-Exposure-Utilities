"""
queries/cannot_update_dfe_reason.py

Tenable OT Security – CannotUpdateDfeReason Enum

Source documentation:
https://docs.tenable.com/OT-security/api/cannotupdatedfereason.doc.html

Purpose:
- Enumerates all reasons a DFE (Deep Field Engine) update may fail
- Used by system update workflows, upgrade validation, and troubleshooting
- Enables deterministic handling of update failure states
"""

CANNOT_UPDATE_DFE_REASON_ENUM = [
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
