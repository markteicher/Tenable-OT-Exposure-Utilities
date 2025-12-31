"""
queries/asset_types.py

Tenable OT Security – Asset Types GraphQL Queries

Source documentation:
https://docs.tenable.com/OT-security/api/assettype.doc.html

Purpose:
- Enumerate ALL AssetType values defined by Tenable OT
- Used for asset normalization, reporting, filtering, and joins
- Canonical reference for OT / IT / IoT / Industrial asset classification
- Explicitly defined to match Tenable OT documentation
"""

ASSET_TYPES = [
    "Unknown",
    "NetworkDevice",
    "Radio",
    "Repeater",
    "Converter",
    "Firewall",
    "AccessPoint",
    "Hub",
    "Gateway",
    "SerialEthernetBridge",
    "Switch",
    "Router",
    "OtDevice",
    "IndustrialPrinter",
    "IndustrialNetworkDevice",
    "IndustrialGateway",
    "IndustrialSwitch",
    "IndustrialRouter",
    "Iot",
    "Projector",
    "Panel",
    "StorageDevice",
    "VoipDevice",
    "Mobile",
    "MedicalDevice",
    "Tablet",
    "SmartTv",
    "SmartHub",
    "LightingControl",
    "HvacModule",
    "AccessControlSystem",
    "BarcodeScanner",
    "SmartSensor",
    "ThreeDPrinter",
    "Printer",
    "Ups",
    "Camera",
    "Server",
    "FileServer",
    "WebServer",
    "VirtualServer",
    "VideoManagementSystem",
    "SecurityAppliance",
    "TenableIcp",
    "TenableEm",
    "TenableSensor",
    "DomainController",
    "FieldDevice",
    "Actuator",
    "Drive",
    "IndustrialSensor",
    "Inverter",
    "Relay",
    "RemoteIo",
    "PowerMeter",
    "OtServer",
    "Historian",
    "DataLogger",
    "Hmi",
    "Workstation",
    "VirtualWorkstation",
    "OtWorkstation",
    "Eng",
    "Controller",
    "BackplaneModule",
    "PowerSupply",
    "Io",
    "Cp",
    "Cnc",
    "Robot",
    "Bms",
    "Rtu",
    "Ied",
    "Dcs",
    "Plc"
]
