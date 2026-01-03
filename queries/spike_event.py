# queries/spike_event.py
#
# Tenable OT Security – SpikeEvent GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/spikeevent.doc.html
#
# Purpose:
# - Possible spike-related events used in Spike Policies

SPIKE_EVENT_ENUM_NAME = "SpikeEvent"

SPIKE_EVENT = [
    "DataSpikeDetected",
    "ConversationCountSpikeDetected",
]
