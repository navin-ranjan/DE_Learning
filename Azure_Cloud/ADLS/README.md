# Azure Data Lake Storage (ADLS)

## Core Theory Concepts (Must Know)
- Separation of storage and compute in modern data platforms
- Namespace design for analytics workloads (partition paths and discoverability)
- Security model layering (RBAC + ACL + network controls)
- Throughput and small-file tradeoffs in distributed query engines
- Durability, redundancy options (LRS/ZRS/GRS), and disaster recovery strategy
- Cost model: transactions, capacity, retrieval, and lifecycle effects

## Fundamentals
- What is ADLS Gen2?
- ADLS Gen1 (legacy) vs Gen2
- Blob Storage vs ADLS
- Hierarchical Namespace
- Use Cases in Data Engineering

## Storage Concepts
- Storage Accounts
- Containers (File Systems)
- Directories & Files
- Blob Types (Block, Append, Page)
- Access Tiers (Hot, Cool, Archive)

## Access Control & Security
- Azure RBAC (Role-Based Access Control)
- ACLs (Access Control Lists)
- POSIX-like Permissions
- Shared Access Signatures (SAS)
- Managed Identities
- Azure Key Vault Integration
- Private Endpoints
- Firewall Rules
- Encryption at rest and in transit
- Soft delete, versioning, immutability policies

## Data Organization
- Folder Structure Best Practices
- Partitioning Strategies
- File Formats (Parquet, Delta, Avro, JSON, CSV)
- Delta Lake on ADLS
- Data Lake Zones (Raw, Bronze, Silver, Gold)

## Working with ADLS

### Using Azure Portal
- Create Storage Account
- Enable Hierarchical Namespace
- Upload/Download Files
- Manage ACLs

### Using Azure CLI
- Create Storage Account
- Create Containers
- Upload/Download Files
- Manage Permissions

### Using Python (Azure SDK)
- azure-storage-blob library
- azure-storage-file-datalake library
- Authentication (Connection String, SAS, Managed Identity)
- Read/Write Operations
- Directory Operations
- ACL Management

### Using PySpark
- Reading from ADLS
- Writing to ADLS
- Configuration (abfss://)
- Authentication Methods

## Integration with Services
- ADLS + Azure Data Factory
- ADLS + Azure Databricks
- ADLS + Azure Synapse
- ADLS + Azure Functions
- ADLS + Azure Event Grid

## Performance & Optimization
- Throughput Optimization
- File Size Recommendations
- Partitioning for Query Performance
- Caching Strategies

## Data Lifecycle Management
- Lifecycle Management Policies
- Auto-tiering
- Auto-deletion
- Archive Strategies

## Monitoring & Logging
- Azure Monitor
- Diagnostic Settings
- Storage Analytics Logs
- Metrics & Alerts

## Best Practices
- Naming Conventions
- Security Best Practices
- Cost Optimization
- Data Governance
- Backup & Disaster Recovery

## Useful Resources
- Theory Notes: `./adls_theory.md`
- Official Documentation: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction
- Microsoft Learn: https://learn.microsoft.com/en-us/training/paths/data-lake-storage-modernize-data-platform/
