"""
queries/icp_policy_field.py

Tenable OT Security – IcpPolicyField GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/icppolicyfield.doc.html

Purpose:
- Enumerates fields available for ICP policy queries
"""

ICP_POLICY_FIELD_ENUM_NAME = "IcpPolicyField"

ICP_POLICY_FIELDS = [
    "id",
    "index",
    "title",
    "level",
    "disabled",
    "archived",
    "event",
    "schema",
    "continuous",
    "snapshot",
    "system",
    "key",
    "site",
]
