# queries/purdue_level.py
#
# Tenable OT Security – PurdueLevel GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/purduelevel.doc.html
#
# Purpose:
# - Enumerates Purdue Model levels for asset classification and policy queries

PURDUE_LEVEL_ENUM_NAME = "PurdueLevel"

PURDUE_LEVELS = [
    "UnknownLevel",
    "Level0",
    "Level1",
    "Level2",
    "Level3",
    "Level4",
]
