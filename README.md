# Tenable-OT-Exposure-Utilities
Tenable OT Exposure Utilities

- Tenable OT Exposure is a very complex solution with leftover components from Indegy ICS 
- Compared to other OT Solutions from licensing to physical hardware to being able to extract the information due to limited export capabilities via .json, .csv, .pdf. or PowerBI
- It requires months of testing versus 30-60 days 

⚠️ Disclaimer

## NO SIMPLE QUICKSTART

There is NO simple Quickstart as advertised by Tenable regarding up and running in less than 5 days in an Enterprise grade environment. 

There is shipping of actual physical hardware, there are network placement requests, placing the physical appliances at the correct location.

30+ step for configuration for each physical appliance, more for virtual (they don't provide much value for an Enterprise Grade environment)

Tenable's Quickstart OT effort does not include API testing at all, which makes it much more complex on Enterprises are evaluating OT/IOT Enterprise grade solutions without the following:

- A documented Requirements Traceability Matrix Document
- Granular Example Use Case Document
- Pre-defined granular project plan
- User Documentation Review
- Installation Review
- Initial Setup Review
- 'official' defect tracker
- High Level Testing Document
- High Level Executive Presentation
- Detailed Testing Document
- Detailed Report


as compared to other OT Enterprise Grade solutions, this platform needs lots of work versus just advertising as part of the Unifified Exposure Management platform.

⚠️ Disclaimer

- Only 3 GraphQL examples provided, really not useful if advertising the platform is Enterprise Grade

- GraphQL API for Tenable OT is poorly documented, it takes years to master GraphQL Schema archaeology + API reconstruction + OT domain modeling then apply that to Tenable's attempt after Indegy ICS acquisition where most Enterprises will leverage less than 1% of the API capabilities

- Only focus on OT Vulnerabilities that only provides limited view and multiple column selection to provide visible data to the authorized administrators, no Enterprise would grant access to asset owners at scale for limited views on discovered assets.
- 
- The User Interface is not designed for large scale administration for asset owners, no operational management for operational utilization, health, user monitoring, activity day over day, week over week, month over month, quarter over quarter, year over year.
- 
- No User Access Reviews, No Asset fatigure review, no Policy fatigure is covered.
  



## Skills Required

- Years of Extensive GraphQL Experience

- Years of schema design and harvesting

- Years of reverse-engineering/reverse mapping to provide Executive Level, Senior Management, Asset Custodians at a glance Visualizations without requiring access to the TenableOne or TenableOT Platform.

- Schema-first thinking (types, enums, connections, edges)

- Cursor-based pagination (not offset-based)

- How enums actually constrain valid queries

- How permissions and capabilities gate fields are implemented

- How vendor-specific modeling choices work

⚠️ Disclaimer


Use of this package are not covered by any license, warranty, or support agreement you may have with Tenable.
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

	
