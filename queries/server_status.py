# queries/server_status.py
#
# Tenable OT Security – ServerStatus GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/serverstatus.doc.html
#
# Purpose:
# - Connection and authentication status when communicating with a server

SERVER_STATUS_ENUM_NAME = "ServerStatus"

SERVER_STATUS = [
    "Ok",
    "Unreachable",
    "BadCredentials",
    "NoPermission",
    "UnknownError",
    "InProgress",
    "SessionsLimitExceeded",
]
