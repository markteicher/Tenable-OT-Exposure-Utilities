"""
queries/children_policy_hit_field.py

Tenable OT Security – ChildrenPolicyHitField GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/childrenpolicyhitfield.doc.html

Purpose:
- Enumerates sortable and selectable fields for child policy hit queries
"""

CHILDREN_POLICY_HIT_FIELD_ENUM_NAME = "ChildrenPolicyHitField"

CHILDREN_POLICY_HIT_FIELDS = [
    "eventId",
    "type",
    "time",
    "srcInterface",
    "srcMac",
    "srcIP",
    "dstInterface",
    "dstMac",
    "dstIP",
    "completion",
    "payloadSize",
    "protocolRaw",
    "protocol",
    "hasDetails",
    "continuous",
    "port",
    "resolved",
    "resolvedTs",
    "resolvedUser",
    "comment",
    "findingId",
    "hitId",
    "policyId",
    "policyName",
    "policyArchived",
    "logId",
    "severity",
    "category",
]
