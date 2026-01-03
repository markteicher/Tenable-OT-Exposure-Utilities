# queries/sort_direction.py
#
# Tenable OT Security – SortDirection GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/sortdirection.doc.html
#
# Purpose:
# - Supported sort directions with explicit NULL ordering

SORT_DIRECTION_ENUM_NAME = "SortDirection"

SORT_DIRECTION = [
    "AscNullFirst",
    "AscNullLast",
    "DescNullFirst",
    "DescNullLast",
]
