# queries/policy_hit_field.py
#
# Tenable OT Security – PolicyHitField GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/policyhitfield.doc.html
#
# Purpose:
# - Enumerates selectable fields for PolicyHit queries

POLICY_HIT_FIELD_ENUM_NAME = "PolicyHitField"

POLICY_HIT_FIELDS = [
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
    "aggregationId",
    "findingId",
    "hitId",
    "policyId",
    "policyName",
    "policyArchived",
    "logId",
    "severity",
    "category",
]
