# queries/rdp_failure_code.py
#
# Tenable OT Security – RdpFailureCode GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/rdpfailurecode.doc.html
#
# Purpose:
# - Enumerates RDP connection failure reasons reported by the platform

RDP_FAILURE_CODE_ENUM_NAME = "RdpFailureCode"

RDP_FAILURE_CODES = [
    "UnknownFailureCode",
    "SslRequiredByServerFailureCode",
    "SslNotAllowedByServerFailureCode",
    "SslCertNotOnServerFailureCode",
    "InconsistentFlagsFailureCode",
    "HybridRequiredByServerFailureCode",
    "SslWithUserAuthRequiredByServerFailureCode",
]
