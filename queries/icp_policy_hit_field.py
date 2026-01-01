"""
queries/icp_policy_hit_field.py

Tenable OT Security – IcpPolicyHitField GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/icppolicyhitfield.doc.html

Purpose:
- Enumerates fields available for ICP policy hit queries
"""

ICP_POLICY_HIT_FIELD_ENUM_NAME = "IcpPolicyHitField"

ICP_POLICY_HIT_FIELDS = [
    "eventId",
    "type",
    "time",
    "srcMac",
    "srcIP",
    "dstMac",
    "dstIP",
    "completion",
    "protocolRaw",
    "protocolNiceName",
    "port",
    "hitId",
    "policyId",
    "policyName",
    "policyArchived",
    "severity",
    "category",
    "resolved",
    "resolvedTs",
    "comment",
    "site",
]
