# 03 - Non-Relational Data on Azure (DP-900)

## Learning Goals

By the end of this tutorial, you should be able to:

- Distinguish Azure Blob, Files, and Table storage use cases
- Understand non-relational data models
- Explain Azure Cosmos DB core concepts for DP-900
- Choose the right non-relational service for common scenarios

---

## 3.1 Azure Storage Services

### Azure Blob Storage

#### What It Is

Azure Blob Storage is Microsoft's massively scalable object storage service designed for storing unstructured data. It can hold trillions of objects spanning multiple petabytes of data. It's the foundation for many Azure data solutions and handles everything from small documents to massive video files.

**Key characteristics:**
- Object storage (not file system or block storage)
- HTTP/HTTPS accessible
- Three access tiers for cost optimization
- Built-in redundancy for durability

---

#### Common Data Types Stored

Blob Storage excels at storing:

- **Images and media:** Product images, user photos, videos
- **Documents:** PDFs, Word documents, Excel files
- **Log files:** Application logs, server logs, clickstream data
- **Backups:** Database backups, file backups, disaster recovery archives
- **Data lake files:** Raw data for analytics, Parquet/CSV files

---

#### Important Concepts

**Containers:**
- Containers organize blobs (similar to folders)
- Every blob must belong to a container
- Container names must be lowercase
- Access policies can be set at container level

```
Storage Account
├── container-images/
│   ├── product-001.jpg
│   ├── product-002.jpg
│   └── profile/
│       └── user-123.png
├── container-logs/
│   └── app-2024-01-15.log
└── container-backups/
    └── db-backup-2024.bak
```

**Access Tiers:**

| Tier | Best For | Storage Cost | Access Cost | Retrieval |
|------|----------|--------------|-------------|-----------|
| **Hot** | Frequently accessed data | Higher | Lower | Immediate |
| **Cool** | Infrequent access (>30 days) | Lower | Higher | Immediate |
| **Archive** | Rarely accessed (>180 days) | Lowest | Highest | Hours |

**Lifecycle Management:**
- Create rules to automatically move blobs between tiers
- Delete old blobs automatically
- Example: Move logs older than 90 days to Cool, delete after 1 year

---

#### When to Use Blob Storage

- **Data lake foundation:** Store massive amounts of raw data for analytics
- **Backup and archive:** Long-term storage for disaster recovery
- **Static content delivery:** Images, videos served to users
- **Big data workloads:** Store files for Spark, Databricks, Synapse processing
- **Disaster recovery:** Geo-redundant storage for business continuity

**When NOT to use:**
- Need file system features (use Azure Files instead)
- Need database-like queries (use Cosmos DB or SQL instead)
- Small files accessed frequently with high rename/move operations

---

### Azure Files

#### What It Is

Azure Files provides fully managed network file shares in the cloud. It offers Server Message Block (SMB) and Network File System (NFS) protocols, making it compatible with applications designed for traditional file shares.

**Key characteristics:**
- Standard file share protocols (SMB 3.0, NFS 4.1)
- Accessible from multiple VMs simultaneously
- Fully managed (no OS to maintain)
- Cloud-native file storage

---

#### When to Use Azure Files

**Lift-and-shift applications:**
- Applications originally designed for file shares
- Legacy applications that expect network drives
- Minimize code changes when migrating to Azure

**Shared file access:**
- Configuration files shared across multiple VMs
- Log files that multiple applications need to access
- Application deployment files
- Development files shared in a team

**Simple scenarios:**
- Need file system semantics (directories, permissions)
- Multiple processes need to access same files
- Existing backup solutions target file shares

**Example use cases:**
- A Windows application expects `F:\Data\config.xml`
- Create Azure Files share, mount as F: drive
- Application works without modification

---

#### Key Point: Blob vs Files

| Feature | Azure Blob Storage | Azure Files |
|---------|-------------------|-------------|
| **Access** | HTTP/REST API | SMB/NFS protocols |
| **Structure** | Flat (containers + blobs) | Hierarchical (directories) |
| **Use case** | Object storage, data lakes | File shares, lift-and-shift |
| **Permissions** | Azure AD, SAS tokens | NTFS permissions |
| **Concurrent access** | Optimized for single writer | Designed for multiple writers |

**Simple distinction:**
- Blob = "Drop files here for storage/analytics"
- Files = "Mount this as a drive letter"

---

### Azure Table Storage

#### What It Is

Azure Table Storage is a NoSQL key-attribute store that provides simple design with massive scale. It's part of Azure Storage accounts and offers extremely low latency for point lookups.

**Key characteristics:**
- NoSQL key-value storage
- Flexible schema (different fields per row)
- Extremely scalable (billions of entities)
- Low cost for simple storage patterns

---

#### Data Design

**PartitionKey and RowKey:**

Every entity in Table Storage has two mandatory properties:

- **PartitionKey:** Determines data distribution across storage nodes
- **RowKey:** Uniquely identifies entity within partition

```
Table: CustomerProfiles
-----------------------------------------
PartitionKey | RowKey  | Email         | City
-------------|---------|---------------|--------
USA          | 1001    | alice@.com    | Seattle
USA          | 1002    | bob@.com      | NYC
UK           | 2001    | charlie@.com  | London
```

**Query efficiency:**
- Most efficient: Query by PartitionKey + RowKey
- Efficient: Query by PartitionKey with RowKey range
- Less efficient: Query across partitions (expensive)
- Least efficient: Table scan (avoid)

**Flexible schema:**
- No predefined schema for all rows
- Each row can have different properties
- Properties have types (String, Int64, Binary, etc.)

---

#### When to Use Table Storage

- **Simple key-lookup patterns:** User profiles, device metadata
- **Large scale with simple access:** Billions of simple records
- **Low-cost storage:** When cost is primary concern
- **Metadata storage:** Storing metadata about blobs, files
- **Session state:** Simple session data

**Good fit:**
```
Retrieve user profile by userId → Perfect for Table Storage
Query users by age, city, interests → Use Cosmos DB or SQL instead
```

---

## Non-Relational Data Models (Conceptual)

Understanding different data models helps you choose the right database:

### Key-Value Model

**Concept:** Each record has a unique key with an associated value (which can be simple or complex).

**How it works:**
- Store: `key` → `value`
- Retrieve: Give me value for `key`
- No querying by value—must know the key

**Best for:**
- Session storage (user login tokens)
- User profiles (retrieve by userId)
- Caching layers
- Configuration data

**Azure services:** Redis Cache, Azure Table Storage

---

### Document Model

**Concept:** Store JSON-like documents with flexible schemas. Each document can have different fields.

**How it works:**
- Documents are self-contained
- No fixed schema—documents in same container can have different fields
- Query by any field (not just key)
- Supports nested objects and arrays

**Best for:**
- Product catalogs (different attributes per product)
- Content management
- Event sourcing
- Applications with evolving requirements

**Azure services:** Azure Cosmos DB (SQL API, MongoDB API)

---

### Column-Family Model

**Concept:** Organize data into column families rather than rows. Optimized for queries across wide tables.

**How it works:**
- Data grouped in column families
- Each row can have different columns
- Optimized for read/write of many columns
- Good for time-series and event data

**Best for:**
- Time-series data (sensor readings, stock prices)
- Event logging (user actions, system events)
- Massive datasets with sparse columns
- Write-heavy workloads

**Azure services:** Azure Cosmos DB (Cassandra API)

---

### Graph Model

**Concept:** Model data as nodes (entities) and edges (relationships). Relationships are first-class citizens.

**How it works:**
- Nodes store entity data
- Edges store relationships between nodes
- Traverse relationships efficiently
- Query patterns: "Find friends of friends"

**Best for:**
- Social networks
- Recommendation engines
- Fraud detection
- Network analysis

**Azure services:** Azure Cosmos DB (Gremlin API)

---

### Exam Tip: Match Model to Access Pattern

> "Choose the data model based on how you'll access the data, not just how the data looks."

| Access Pattern | Best Model |
|---------------|------------|
| Get value by known key | Key-Value |
| Flexible documents, evolving schema | Document |
| Query by multiple fields | Document |
| Massive wide tables, time-series | Column-Family |
| Complex relationships, traversal | Graph |

---

## 3.2 Azure Cosmos DB

### What Cosmos DB Solves

Azure Cosmos DB is Azure's globally distributed, multi-model database service. It was designed from the ground up for global scale with guaranteed low latency and high availability.

**Core capabilities:**

1. **Global distribution:** Replicate data to any Azure region with single-digit millisecond latency worldwide

2. **Low-latency access:** Guaranteed <10ms read latency at the 99th percentile

3. **High availability:** 99.999% availability SLA with automatic failover

4. **Elastic throughput:** Scale RU/s up or down as needed

5. **Multi-model access:** Use SQL, MongoDB, Cassandra, Gremlin, or Table APIs with the same underlying data

---

### Partitioning

Cosmos DB scales horizontally by distributing data across multiple physical partitions.

#### How Partitioning Works

**Logical partitions:**
- Data is divided based on PartitionKey value
- All items with same PartitionKey value are together
- Each logical partition maxes at 20 GB

**Physical partitions:**
- Azure creates physical partitions based on throughput
- Multiple logical partitions can share a physical partition
- Azure manages physical partition distribution

#### Partition Key Choice (Critical!)

The partition key you choose significantly impacts performance:

**Good partition keys:**
- customerId (if queries filter by customer)
- deviceId (for IoT scenarios)
- tenantId (for multi-tenant apps)

**Characteristics of good keys:**
- High cardinality (many distinct values)
- Queries filter by this field
- Evenly distributes data

**Bad partition keys:**
- Region/Country (low cardinality)
- Status (few values, creates hot partitions)
- Boolean fields (only 2 values)

**Example:**
```json
// Document with partition key = customerId
{
    "id": "order-001",
    "customerId": "cust-123",  // ← Partition key
    "items": [...],
    "total": 150.00
}
```

Query: `SELECT * FROM c WHERE c.customerId = "cust-123"` → Efficient (single partition)
Query: `SELECT * FROM c WHERE c.total > 100` → Expensive (cross-partition)

---

### Throughput (RU/s)

Cosmos DB uses Request Units (RU) to measure throughput. Every database operation consumes RUs based on its complexity.

#### Understanding RU

**What is a RU:**
- Normalized cost for each operation
- Depends on: operation type, data size, consistency level
- 1 RU = read of 1KB document

**RU consumption by operation:**

| Operation | RU Cost (approximate) |
|-----------|----------------------|
| Point read (by key) | 1-5 RU |
| Simple query | 2-10 RU |
| Write | 5-50+ RU |
| Complex query | 10-100+ RU |

**Reading costs less than writing:**
- Reads just retrieve data
- Writes involve indexing, replication

#### Provisioned vs Autoscale

**Provisioned throughput:**
- Fixed RU/s you specify
- Pay for that amount continuously
- Good for predictable workloads

**Autoscale:**
- Scales between min and max RU/s
- Scales up during peak, down during quiet
- Good for variable workloads

**Rate limiting:**
- If you exceed provisioned RU/s → HTTP 429 (Too Many Requests)
- Cosmos DB retries after short wait

---

### Consistency Levels

Cosmos DB offers five consistency levels, trading off between availability, latency, and consistency.

#### From Strongest to Most Relaxed

1. **Strong Consistency**
   - Always read latest committed write
   - Guarantees: No stale reads
   - Tradeoff: Higher latency, potential unavailability during regional failures

2. **Bounded Staleness**
   - Reads within K versions or T time of latest write
   - Guarantees: Staleness bounded by you
   - Tradeoff: Lower latency than strong

3. **Session Consistency** (Most popular)
   - Guarantees monotonic reads/writes within your session
   - Guarantees: You see your own writes
   - Tradeoff: Lower latency for most scenarios

4. **Consistent Prefix**
   - Guarantees: Never see out-of-order writes
   - Tradeoff: May see stale reads

5. **Eventual Consistency**
   - Highest availability, lowest latency
   - Guarantees: Reads will eventually be consistent
   - Tradeoff: May see stale data briefly

#### Consistency Tradeoff Visual

```
Strong ←——→ Eventual
 |              |
High latency   Low latency
Lower avail    Higher avail
```

**Exam tip:** For DP-900, know that:
- Strong = highest consistency, highest latency
- Eventual = lowest consistency, lowest latency
- Session = most popular, good balance

---

### Cosmos DB APIs

Cosmos DB supports multiple APIs, allowing you to use familiar programming models:

| API | Data Model | Use When |
|-----|------------|----------|
| **SQL (Core)** | JSON documents | Want SQL-like queries over JSON |
| **MongoDB** | BSON documents | Existing MongoDB apps |
| **Cassandra** | Wide columns | Existing Cassandra apps |
| **Gremlin** | Graph | Graph/traversal queries |
| **Table** | Key-value | Existing Azure Table apps |

**Key point:** These are different APIs to the SAME Cosmos DB database. You choose based on:
- Existing application code
- Team skills
- Query requirements

**SQL API query example:**
```sql
SELECT * FROM c WHERE c.customerId = "cust-123"
```

**MongoDB query example:**
```javascript
db.customers.find({ customerId: "cust-123" })
```

---

## Service Choice Examples

Match the scenario to the right service:

### Scenario 1: Store Millions of Product Images

**Answer:** Azure Blob Storage

**Reason:** Unstructured data, massive scale, cost-effective, designed for this exact use case.

---

### Scenario 2: Shared Folder for Legacy App Config Files

**Answer:** Azure Files

**Reason:** Lift-and-shift scenario expecting file shares. Azure Files provides SMB access without code changes.

---

### Scenario 3: Globally Distributed App Profiles with Low-Latency Reads/Writes

**Answer:** Azure Cosmos DB

**Reason:** Global distribution with single-digit millisecond latency, multi-region writes, elastic scaling.

---

### Scenario 4: Low-Cost Simple Key-Attribute Records

**Answer:** Azure Table Storage

**Reason:** Simple key-value model, extremely low cost, billions of entities, simple access patterns.

---

## Mini Hands-On Flow

### Step 1: Create a Storage Account
1. Azure Portal → Create Storage Account
2. Choose: Subscription, Resource Group, Name
3. Configure: Performance (Standard), Redundancy (LRS/GRS)
4. Review and Create

### Step 2: Create Blob Container and Upload Files
1. Navigate to Storage Account → Data storage → Containers
2. Create container (e.g., "documents")
3. Upload sample files (images, PDFs, CSV)
4. Set access tier appropriately

### Step 3: Configure Lifecycle Rule
1. Go to Lifecycle Management
2. Create rule: "Move older blobs to Cool tier"
3. Set filter: All blobs, older than 30 days
4. Action: Move to Cool tier
5. Save rule

### Step 4: Create Cosmos DB Account (SQL API)
1. Azure Portal → Create Cosmos DB
2. Choose: Azure Cosmos DB for NoSQL (SQL API)
3. Configure: Subscription, Resource Group
4. Configure: Account name, Location, Capacity mode
5. Configure: Global distribution (add regions)
6. Create

### Step 5: Create Database and Container
1. Navigate to Cosmos DB → Data Explorer
2. Create Database (e.g., "RetailDB")
3. Create Container with partition key (e.g., `/customerId`)
4. Set throughput (e.g., 400 RU/s)

### Step 6: Insert and Query Documents
1. Use Data Explorer to add items:
   ```json
   {
     "id": "order-001",
     "customerId": "cust-123",
     "total": 150.00,
     "items": [{"sku": "A10", "qty": 2}]
   }
   ```
2. Query by partition key:
   ```sql
   SELECT * FROM c WHERE c.customerId = "cust-123"
   ```
3. Observe RU charge in query metrics

### Step 7: Observe RU Usage
1. Check "Query Metrics" for RU cost
2. Try different queries and observe RU variation
3. Understand how query complexity affects RU consumption

---

## Expected Learning Outcomes

After this hands-on exercise, you should understand:

- **Non-relational service differentiation:** When to use Blob, Files, Table, Cosmos DB
- **Partition key impact:** How key choice affects scaling and performance
- **Cosmos DB fundamentals:** Consistency levels, throughput (RU/s), APIs

---

## Common Mistakes to Avoid

1. **Choosing partition key without analyzing query pattern**
   - Always analyze how you'll query before choosing partition key
   - Wrong key = hot partitions and throttling

2. **Assuming Blob storage behaves like a file share**
   - Blob is object storage (HTTP access)
   - Use Azure Files for SMB/NFS access

3. **Ignoring RU costs during design**
   - Complex queries consume many RU
   - Design queries to use partition keys
   - Monitor RU consumption in production

---

## Quick Self-Check Questions

1. **Can you explain Blob vs Files in one sentence each?**
   - Blob: Object storage for unstructured data, accessed via HTTP
   - Files: Managed file shares accessed via SMB/NFS protocols

2. **Can you explain why partition keys matter in Cosmos DB?**
   - Partition key determines data distribution and query efficiency
   - Good key = even distribution, efficient queries
   - Bad key = hot partitions, throttling

3. **Can you list at least three Cosmos DB APIs?**
   - SQL (Core) API
   - MongoDB API
   - Cassandra API
   - Gremlin API
   - Table API
