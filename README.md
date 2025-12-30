# Tenable-OT-Exposure-Utilities
Tenable OT Exposure Utilities


⚠️ Disclaimer

This tool is not an official Tenable product.

Use of this software is not covered by any license, warranty, or support agreement you may have with Tenable.
All functionality is implemented independently using publicly available Tenable OT Exposure API documentation.

# 🏭 Tenable OT GraphQL Exporter

## Overview
Enterprise-grade GraphQL query framework for **Tenable OT Security**.  
Designed to safely extract, paginate, and export **OT assets, events, sensors, policies, users, and operational telemetry** using Tenable OT’s native GraphQL API.

This project focuses on **validated, non-minimal GraphQL queries** that align directly with Tenable OT’s documented schema and operational data model.

---

## 🚀 Key Capabilities

### 🧠 OT Asset Intelligence
| Feature | Description |
|------|-------------|
| 🏗️ Asset Inventory | Full OT asset extraction including type, vendor, firmware, serial, OS, Purdue level |
| 🧬 Asset Classification | Asset types, categories, roles, safety-rated flags |
| 🌐 Network Context | IPs, MACs, VLANs, segments, zones |
| 🧱 Purdue Model Mapping | Native Purdue level support (L0–L5) |
| ⏱️ Lifecycle Visibility | First seen, last seen, update timestamps |
| 🧾 Revision Tracking | Asset revisions and configuration changes |

---

### 🔍 Detection & Risk Analytics
| Feature | Description |
|------|-------------|
| 🚨 OT Events | Security, policy, and operational events |
| 📊 Aggregated Event Metrics | 24h / 7d / 30d event aggregation |
| ⚠️ Severity & Category | Event severity, family, category, protocol |
| 🧩 Policy Context | Event-to-policy attribution |
| 🔄 Continuous vs Snapshot | Supports both continuous and snapshot detections |

---

### 🛡️ Vulnerability & Plugin Intelligence
| Feature | Description |
|------|-------------|
| 🔌 OT Plugins | Plugin metadata, source, family, severity |
| 📈 Risk Metrics | VPR, CVSS, unresolved events |
| 🧠 Asset Enrichment | Extended plugin details and references |
| 🔗 Asset Impact | Plugin-to-asset relationships |

---

### 🛰️ Sensor & Infrastructure Health
| Feature | Description |
|------|-------------|
| 📡 ICP Sensor Status | Sensor connectivity, health, last seen |
| 🧭 Sensor Types | Component and protocol-specific sensors |
| 🧪 BACnet & OT Protocol Visibility | BACnet object types, protocol metadata |
| 🕒 Telemetry Timelines | Time-based operational metrics |

---

### 👥 User & Access Intelligence
| Feature | Description |
|------|-------------|
| 👤 Users | User accounts and roles |
| 🔑 Authentication Validation | GraphQL-based API key verification |
| 🧾 User Activity | Action types, policy interactions |
| 🔍 User Visibility | User-driven operational actions |

---

## 📊 Supported GraphQL Domains

The exporter includes validated GraphQL coverage for:

- Assets
- Asset Fields
- Asset Types
- Asset Categories
- Events
- Event Policies
- Action Types
- Plugins
- Plugin Details
- Sensor Status
- ICP Sensor Fields
- BACnet Object Types
- Component Types
- Purdue Levels
- Core OS Versions
- Users
- System Logs

Each domain is implemented as a **standalone, paginated GraphQL query** aligned with Tenable OT documentation.

---

## 🧱 Architecture Highlights

| Component | Purpose |
|--------|--------|
| 🧠 GraphQL Templates | Schema-aligned, non-minimal queries |
| 🔁 Pagination Engine | Cursor-based extraction |
| 🧪 Validation Layer | API key and permission validation |
| 📦 Export Formats | JSON and CSV ready |
| ⏱️ Rate Control | Retry, backoff, and timeout discipline |
| 🧯 Error Normalization | Structured failure events |

---

## 📁 Project Structure
	
