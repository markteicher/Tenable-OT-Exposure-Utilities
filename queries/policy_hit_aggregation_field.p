# queries/policy_hit_aggregation_field.py
#
# Tenable OT Security – PolicyHitAggregationField GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/policyhitaggregationfield.doc.html
#
# Purpose:
# - Enumerates selectable aggregation fields for Policy Hit queries

POLICY_HIT_AGGREGATION_FIELD_ENUM_NAME = "PolicyHitAggregationField"

POLICY_HIT_AGGREGATION_FIELDS = [
    "resolved",
    "resolvedTs",
    "resolvedUser",
    "comment",
    "aggregationId",
    "lastEventTime",
    "policyId",
    "policyName",
    "policyArchived",
    "severity",
    "type",
    "srcMac",
    "srcIP",
    "dstMac",
    "dstIP",
    "protocolRaw",
    "category",
    "protocolNiceName",
    "parentId",
    "parentLogId",
    "parentEventTime",
    "parentFindingId",
    "resolutionDuration",
]
