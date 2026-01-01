"""
queries/expr_op.py

Tenable OT Security – ExprOp GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/exprop.doc.html

Purpose:
- Enumerates supported expression operators used in filters and exclusions
"""

EXPR_OP_ENUM_NAME = "ExprOp"

EXPR_OPS = [
    "Equal",
    "NotEqual",
    "Greater",
    "Less",
    "GreaterEqual",
    "LessEqual",
    "In",
    "NotIn",
    "Between",
    "NotBetween",
    "And",
    "Or",
    "Contains",
    "NotContains",
    "Like",
    "NotLike",
    "SubnetContainsEqual",
]
