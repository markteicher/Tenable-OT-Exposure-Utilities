# queries/directive_location.py
#
# Tenable OT Security – __DirectiveLocation GraphQL Enum
#
# Source documentation:
# https://docs.tenable.com/OT-security/api/directivelocation.spec.html
#
# Purpose:
# - Defines the valid locations where a GraphQL directive may appear

DIRECTIVE_LOCATION_ENUM_NAME = "__DirectiveLocation"

DIRECTIVE_LOCATIONS = [
    "QUERY",
    "MUTATION",
    "SUBSCRIPTION",
    "FIELD",
    "FRAGMENT_DEFINITION",
    "FRAGMENT_SPREAD",
    "INLINE_FRAGMENT",
    "VARIABLE_DEFINITION",
    "SCHEMA",
    "SCALAR",
    "OBJECT",
    "FIELD_DEFINITION",
    "ARGUMENT_DEFINITION",
    "INTERFACE",
    "UNION",
    "ENUM",
    "ENUM_VALUE",
    "INPUT_OBJECT",
    "INPUT_FIELD_DEFINITION",
]
