"""
queries/feed_type.py

Tenable OT Security – FeedType GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/feedtype.doc.html

Purpose:
- Enumerates feed sources used by the platform
"""

FEED_TYPE_ENUM_NAME = "FeedType"

FEED_TYPES = [
    "NessusPluginSet",
    "SuricataRuleSet",
    "Pii",
]
