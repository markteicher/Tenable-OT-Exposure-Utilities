"""
queries/credential_schema_type.py

Tenable OT Security – CredentialSchemaType GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/credentialschematype.doc.html

Purpose:
- Defines supported credential schema types
"""

CREDENTIAL_SCHEMA_TYPE_ENUM_NAME = "CredentialSchemaType"

CREDENTIAL_SCHEMA_TYPE_FIELDS = [
    "BasicSchema",
    "BasicSchemaWithRole",
    "PasswordOnlySchema",
    "SnmpV2Schema",
    "SnmpV3Schema",
]
