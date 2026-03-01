# Azure DP-900 (Data Fundamentals) - Organized Topic Guide

This README organizes the full DP-900 syllabus into a practical study outline.

Source baseline: Microsoft Learn Study Guide for DP-900 (skills measured as of **November 1, 2024**).

## Table of Contents

1. [Exam Overview](#exam-overview)
2. [Domain 1: Core Data Concepts (25-30%)](#domain-1-core-data-concepts-25-30)
3. [Domain 2: Relational Data on Azure (20-25%)](#domain-2-relational-data-on-azure-20-25)
4. [Domain 3: Non-Relational Data on Azure (15-20%)](#domain-3-non-relational-data-on-azure-15-20)
5. [Domain 4: Analytics Workload (25-30%)](#domain-4-analytics-workload-25-30)
6. [Detailed Tutorials](#detailed-tutorials)
7. [Quick Revision Checklist](#quick-revision-checklist)
8. [Official References](#official-references)

## Exam Overview

- Exam name: `DP-900: Microsoft Azure Data Fundamentals`
- Focus: fundamental data concepts + Azure data services
- Audience: beginners in cloud data and analytics
- Expected familiarity:
  - Relational and non-relational data
  - Transactional and analytical workloads

---

## Domain 1: Core Data Concepts (25-30%)

### 1.1 Data Representation
- Structured data
  - Fixed schema, rows/columns, relational tables
- Semi-structured data
  - Flexible schema, tags/keys (for example JSON, XML)
- Unstructured data
  - No predefined model (images, videos, documents, audio)

### 1.2 Data Storage Options
- Common file formats
  - CSV, TSV, JSON, XML
  - Parquet/ORC/Avro for analytics scenarios
- Types of databases
  - Relational
  - Non-relational (key-value, document, column-family, graph)

### 1.3 Data Workloads
- Transactional workloads (OLTP)
  - Frequent small writes/reads, low latency, high concurrency
- Analytical workloads (OLAP)
  - Large scans/aggregations, historical trends, BI/reporting

### 1.4 Data Roles and Responsibilities
- Database Administrator (DBA)
  - Availability, backups, security, performance, operations
- Data Engineer
  - Build ingestion/transformation pipelines, model data stores
- Data Analyst
  - Explore data, create reports/dashboards, communicate insights

---

## Domain 2: Relational Data on Azure (20-25%)

### 2.1 Relational Concepts
- Relational characteristics
  - Tables, keys, relationships, constraints, normalization
- Why normalization is used
  - Reduce redundancy, improve integrity, simplify maintenance
- Common SQL statements
  - `SELECT`, `INSERT`, `UPDATE`, `DELETE`
  - `JOIN`, `GROUP BY`, filtering, sorting
- Common database objects
  - Tables, views, indexes, stored procedures, functions

### 2.2 Azure Relational Services
- Azure SQL family
  - Azure SQL Database
  - Azure SQL Managed Instance
  - SQL Server on Azure Virtual Machines
- Open-source relational services on Azure
  - Azure Database for PostgreSQL
  - Azure Database for MySQL

---

## Domain 3: Non-Relational Data on Azure (15-20%)

### 3.1 Azure Storage Capabilities
- Azure Blob Storage
  - Object storage for massive unstructured data
  - Access tiers and lifecycle options
- Azure Files
  - Managed SMB/NFS file shares in Azure
- Azure Table Storage
  - Simple NoSQL key/attribute store for large scale

### 3.2 Azure Cosmos DB
- Core use cases
  - Global distribution, low latency, elastic scale, high availability
- Key concepts
  - Partitioning
  - Throughput (RU/s)
  - Consistency levels
- APIs
  - SQL (Core), MongoDB, Cassandra, Gremlin, Table

---

## Domain 4: Analytics Workload (25-30%)

### 4.1 Large-Scale Analytics Elements
- Data ingestion and processing considerations
  - Batch vs streaming ingestion
  - ETL vs ELT
  - Orchestration and pipeline reliability
- Analytical data store options
  - Data warehouse
  - Data lake
  - Lakehouse
- Cloud services for large-scale analytics
  - Azure Databricks
  - Microsoft Fabric
  - (Related ecosystem services often seen in learning paths: Synapse, Data Factory)

### 4.2 Real-Time Analytics
- Batch vs streaming data differences
  - Latency, processing pattern, and use cases
- Microsoft cloud services for real-time analytics
  - Event ingestion + stream processing services in Azure/Fabric ecosystem

### 4.3 Data Visualization with Power BI
- Power BI capabilities
  - Interactive reports, dashboards, sharing/collaboration
- Data model features
  - Relationships, measures, calculated columns, model design basics
- Choosing effective visuals
  - Match visual type to analytical question and data shape

---

## Detailed Tutorials

For full, step-by-step tutorials for every DP-900 topic, use:

- [Tutorial Index](./tutorials/README.md)
- [01 - Core Data Concepts](./tutorials/01-core-data-concepts.md)
- [02 - Relational Data on Azure](./tutorials/02-relational-data-on-azure.md)
- [03 - Non-Relational Data on Azure](./tutorials/03-non-relational-data-on-azure.md)
- [04 - Analytics Workload](./tutorials/04-analytics-workload.md)

---

## Quick Revision Checklist

- Can explain structured vs semi-structured vs unstructured data
- Can compare OLTP and OLAP workloads
- Can identify Azure SQL service options and when to use each
- Can describe Blob, Files, and Table storage differences
- Can explain Cosmos DB basics: partitioning, RU/s, consistency, APIs
- Can compare batch and streaming analytics
- Can identify Databricks/Fabric roles in analytics pipelines
- Can describe core Power BI modeling and visualization concepts

---

## Official References

- DP-900 study guide (official):
  - https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900
- DP-900 certification page:
  - https://learn.microsoft.com/en-us/credentials/certifications/azure-data-fundamentals/
