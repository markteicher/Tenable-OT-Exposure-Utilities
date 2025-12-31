# Tenable-OT-Exposure-Utilities
Tenable OT Exposure Utilities

Tenable OT Exposure is a very expensive solution compared to other OT Solutions from licensing to physical hardware to being able to extract the information due to limited export capabilities via .json, .csv, .pdf. 

There is NO simple Quickstart as advertised by Tenable regarding up and running in less than 5 days. 

GraphQL API for Tenable OT is poorly documented, it takes day in and day out years to master GraphQL Schema archaeology + API reconstruction + OT domain modeling then apply that to Tenable's attempt after Indegy ICS acquisition where most Enterprises will leverage less than 1% of the API capabilities, only focus on OT Vulnerabilities that only provides views to last 60 days if that through the User Interface. 

Only 3 GraphQL examples provided, really not useful if advertising the platform is Enterprise Grade

Extensive, painstaking schema harvesting, reverse mapping/reverse-engineering to provide Executive Level, Senior Management, Asset Custodians at a glance Visualizations without requiring access to the TenableOne or TenableOT Platform.

## Skills Required

Schema-first thinking (types, enums, connections, edges)

Cursor-based pagination (not offset-based)

How enums actually constrain valid queries

How permissions and capabilities gate fields

How vendor-specific modeling choices work

⚠️ Disclaimer

These
graphql examples are not an official Tenable product.

Use of this graphql queries are not covered by any license, warranty, or support agreement you may have with Tenable.
All functionality is implemented independently using publicly available Tenable OT Exposure API documentation.

# 🏭 Tenable OT GraphQL Exporter

## Overview
Enterprise-grade GraphQL query framework for **Tenable OT Exposure**.  
Designed to extract, paginate, and export **OT assets, events, sensors, policies, users, and operational telemetry** using Tenable OT Exposure's native GraphQL API

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

Each component is implemented as a **standalone, paginated GraphQL query** aligned with Tenable OT Exposure documentation.

---

## 🧱 Architecture Highlights

| Component | Purpose |
|--------|--------|
| 🧠 GraphQL Templates | Schema-aligned queries |
| 🔁 Pagination Engine | Cursor-based extraction |
| 🧪 Validation Layer | API key and permission validation |
| 📦 Export Formats | JSON and CSV ready |
| ⏱️ Rate Control | Retry, backoff, and timeout discipline |
| 🧯 Error Normalization | Structured failure events |

---

## 🎯 Design Principles

- ✅ **Schema-First** – Queries align exactly with Tenable OT Exposure documentation 
- 🔒 **Safe by Default** – Read-only GraphQL operations only  
- 🧪 **Validated** – Designed to run in GraphiQL Playground  
- 🧩 **Composable** – Each query stands alone  

---

## 🧪 Validation & Testing

- Tested using Tenable OT Exposure **GraphiQL Playground**
- Supports cursor-based pagination
- Handles empty result sets gracefully
- Validates API access before extraction

---

## 🏗️ Intended Use Cases

- OT Asset Inventory Export
- Sensor Health Auditing
- OT Event Analysis
- Vulnerability & Plugin Risk Analysis
- IoT/OT discovery, identification, classification mapping based on multiple asset attributes not IP address
- SIEM / Data Lake Ingestion (tool-agnostic)

---

## 📚 References

- Tenable OT Exposure GraphQL Playground  
  https://developer.tenable.com/docs/ot-graphiql-playground

- Tenable OT Exposure API Documentation  
  https://docs.tenable.com/OT-security/api/

---

	
