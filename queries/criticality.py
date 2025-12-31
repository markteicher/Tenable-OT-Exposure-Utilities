"""
queries/criticality.py

Tenable OT Security – Criticality GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/criticality.doc.html

Purpose:
- Defines criticality levels used across OT Security entities
"""

CRITICALITY_ENUM_NAME = "Criticality"

CRITICALITY_FIELDS = [
    "NoneCriticality",
    "LowCriticality",
    "MediumCriticality",
    "HighCriticality",
]
