"""
queries/credentials_category.py

Tenable OT Security – CredentialsCategory GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/credentialscategory.doc.html

Purpose:
- Categorizes credentials as IT or OT
"""

CREDENTIALS_CATEGORY_ENUM_NAME = "CredentialsCategory"

CREDENTIALS_CATEGORY_FIELDS = [
    "ItCredentials",
    "OtCredentials",
]
