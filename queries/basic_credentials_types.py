"""
queries/basic_credentials_types.py

Tenable OT Security – Basic Credentials Types (ENUM)

Source documentation:
https://docs.tenable.com/OT-security/api/basiccredentialstypes.doc.html

Purpose:
- Enumerates all supported basic credential types in Tenable OT
- Used for asset authentication, polling, and secure access configuration
- Supports credential validation, auditing, and export workflows

Notes:
- This file is a direct transcription of the GraphQL enum
- Order and values must remain authoritative and unchanged
"""

BASIC_CREDENTIALS_TYPES = [
    "Ssh",
    "Wmi",
    "Sel",
    "SicamA8000",
    "Bachmann",
    "Moxa",
    "FoxTls",
]
