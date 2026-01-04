# object/aruba_server.py
#
# Tenable OT Security – ArubaServer GraphQL Object
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/arubaserver.doc.html
#
# Purpose:
# - Represents an Aruba server configuration and status

ARUBA_SERVER_OBJECT_NAME = "ArubaServer"

ARUBA_SERVER_FIELDS = [
    "id",
    "hostname",
    "status",
    "username",
    "client",
    "usageInfo",
]
