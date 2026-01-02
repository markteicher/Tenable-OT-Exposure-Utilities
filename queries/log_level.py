"""
queries/log_level.py

Tenable OT Security – LogLevel GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/loglevel.doc.html

Purpose:
- Enumerates supported log verbosity levels
"""

LOG_LEVEL_ENUM_NAME = "LogLevel"

LOG_LEVELS = [
    "debug",
    "info",
    "warn",
    "error",
]
