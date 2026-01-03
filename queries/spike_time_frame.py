# queries/spike_time_frame.py
#
# Tenable OT Security – SpikeTimeFrame GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/spiketimeframe.doc.html
#
# Purpose:
# - Possible time windows used for spike detection

SPIKE_TIME_FRAME_ENUM_NAME = "SpikeTimeFrame"

SPIKE_TIME_FRAME = [
    "FifteenMins",
    "OneHour",
    "FourHours",
    "TwelveHours",
    "OneDay",
    "OneWeek",
    "OneMonth",
]
