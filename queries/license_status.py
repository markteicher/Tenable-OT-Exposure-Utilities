"""
queries/license_status.py

Tenable OT Security – LicenseStatus GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/licensestatus.doc.html

Purpose:
- Represents the current state of the Tenable OT license
"""

LICENSE_STATUS_ENUM_NAME = "LicenseStatus"

LICENSE_STATUS_VALUES = [
    "UnknownLicenseStatus",
    "Uninitialized",
    "WaitingForActivation",
    "Active",
    "SubscriptionExpired",
    "MaintenanceExpired",
    "AssetCountExceeded",
]
