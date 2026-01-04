# queries/user_defined_criticality.py
#
# Tenable OT Security – UserDefinedCriticality GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/userdefinedcriticality.doc.html
#
# Purpose:
# - Represents user-defined criticality levels for assets

USER_DEFINED_CRITICALITY_ENUM_NAME = "UserDefinedCriticality"

USER_DEFINED_CRITICALITY = [
    "NoneCriticality",
    "LowCriticality",
    "MediumCriticality",
    "HighCriticality",
    "_RemoveUserDefinedValue",
]
