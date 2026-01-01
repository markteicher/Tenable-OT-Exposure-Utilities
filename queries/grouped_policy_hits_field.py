"""
queries/grouped_policy_hits_field.py

Tenable OT Security – GroupedPolicyHitsField GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/groupedpolicyhitsfield.doc.html

Purpose:
- Enumerates fields used when grouping policy hits
"""

GROUPED_POLICY_HITS_FIELD_ENUM_NAME = "GroupedPolicyHitsField"

GROUPED_POLICY_HITS_FIELDS = [
    "policyHitsCount",
    "policyId",
    "policyName",
    "type",
    "eventTime",
    "category",
    "resolved",
    "severity",
    "site",
]
