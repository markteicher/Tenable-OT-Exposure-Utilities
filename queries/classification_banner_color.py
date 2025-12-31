"""
queries/classification_banner_color.py

Tenable OT Security – ClassificationBannerColor GraphQL Enum

Source documentation:
https://docs.tenable.com/OT-security/api/classificationbannercolor.doc.html

Purpose:
- Enumerates the available banner color *options* used for classification UI/config
- Note: the enum uses DefaultColor + Color1..Color10 (no named colors)
"""

CLASSIFICATION_BANNER_COLOR_ENUM_NAME = "ClassificationBannerColor"

CLASSIFICATION_BANNER_COLORS = [
    "DefaultColor",
    "Color1",
    "Color2",
    "Color3",
    "Color4",
    "Color5",
    "Color6",
    "Color7",
    "Color8",
    "Color9",
    "Color10",
]
