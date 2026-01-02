# queries/schedule_group_type.py
#
# Tenable OT Security – ScheduleGroupType GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/schedulegrouptype.doc.html
#
# Purpose:
# - Defines the type of schedule group used for policies and scheduling logic

SCHEDULE_GROUP_TYPE_ENUM_NAME = "ScheduleGroupType"

SCHEDULE_GROUP_TYPE = [
    "IntervalGroup",
    "RecurringGroup",
    "Function",
]
