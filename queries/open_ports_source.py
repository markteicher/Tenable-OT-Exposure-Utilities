"""
queries/open_ports_source.py

Tenable OT Security – OpenPortsSource GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/openportssource.doc.html

Purpose:
- Identifies the data source responsible for detecting open ports
"""

OPEN_PORTS_SOURCE_ENUM_NAME = "OpenPortsSource"

OPEN_PORTS_SOURCES = [
    "UnknownSource",
    "ActiveQueries",
    "PortMapping",
    "Conversations",
    "NNM",
    "Nessus",
    "OtAgent",
]
