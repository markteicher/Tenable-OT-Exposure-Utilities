# queries/policy_level.py
#
# Tenable OT Security – PolicyLevel GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/policylevel.doc.html
#
# Purpose:
# - Enumerates policy severity / enforcement levels

POLICY_LEVEL_ENUM_NAME = "PolicyLevel"

POLICY_LEVELS = [
    "None",
    "Low",
    "Medium",
    "High",
]
