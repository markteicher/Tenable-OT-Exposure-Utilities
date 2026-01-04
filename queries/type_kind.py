# queries/type_kind.py
#
# Tenable OT Security – __TypeKind GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/typekind.spec.html
#
# Purpose:
# - Describes the kind of a GraphQL type in schema introspection

TYPE_KIND_ENUM_NAME = "__TypeKind"

TYPE_KINDS = [
    "SCALAR",
    "OBJECT",
    "INTERFACE",
    "UNION",
    "ENUM",
    "INPUT_OBJECT",
    "LIST",
    "NON_NULL",
]
