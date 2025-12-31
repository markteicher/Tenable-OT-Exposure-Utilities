"""
queries/cannot_update_suricata_rules_reason.py

Tenable OT Security – CannotUpdateSuricataRulesReason Enum

Source documentation:
https://docs.tenable.com/OT-security/api/cannotupdatesuricatarulesreason.doc.html

Purpose:
- Enumerates all reasons a Suricata ruleset update may be rejected
- Used for IDS rule update workflows and diagnostics
- Enables deterministic handling of Suricata update failures
"""

CANNOT_UPDATE_SURICATA_RULES_REASON = [
    "Unknown",
    "LicenseInactive",
    "EmLicenseInactive",
    "OldLicense",
    "EmOldLicense",
    "UpdateAlreadyInProgress",
    "Unchanged",
    "NetworkError",
    "InvalidFile",
    "NoSpaceLeftOnDevice",
]
