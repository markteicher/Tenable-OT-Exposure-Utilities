# queries/time_frame.py
#
# Tenable OT Security – TimeFrame GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/timeframe.doc.html
#
# Purpose:
# - Possible time frames for data retrieving

TIME_FRAME_ENUM_NAME = "TimeFrame"

TIME_FRAME = [
    "fifteenMinutes",
    "oneHour",
    "fourHours",
    "twelveHours",
    "oneDay",
    "oneWeek",
    "oneMonth",
    "custom",
]
