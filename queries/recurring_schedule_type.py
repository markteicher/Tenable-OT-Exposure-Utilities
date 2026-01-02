# queries/recurring_schedule_type.py
#
# Tenable OT Security – RecurringScheduleType GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/recurringscheduletype.doc.html
#
# Purpose:
# - Enumerates recurring schedule types for scheduled operations

RECURRING_SCHEDULE_TYPE_ENUM_NAME = "RecurringScheduleType"

RECURRING_SCHEDULE_TYPES = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "EveryDay",
    "MondayToFriday",
]
