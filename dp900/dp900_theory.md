# DP-900 Azure Data Fundamentals - Complete Theory (Extended)

---

# Domain 1: Core Data Concepts (20-25%)

## 1.1 Data Types

### Structured Data
- Organized in rows and columns with fixed schema
- Stored in relational databases
- Examples: SQL databases, Excel spreadsheets
- Easily queried using SQL
- ACID compliant (Atomicity, Consistency, Isolation, Durability)

### Semi-Structured Data
- Does not fit traditional table structure
- Self-describing (contains schema information)
- Examples: JSON, XML, YAML, Avro, Parquet
- Flexible schema - different records can have different fields

### Unstructured Data
- No predefined format or organization
- Examples: Images, videos, audio files, PDFs, documents
- Stored in blob storage or data lakes

---

## 1.2 Data Formats

### CSV
- Plain text, comma-delimited
- Human readable but not efficient for large data

### JSON
- Key-value pairs, hierarchical structure
- Common in web APIs

### Parquet
- Columnar storage format
- Compressed, optimized for analytical queries
- Used in Big Data ecosystems

### Avro
- Row-based serialization
- Schema defined in JSON
- Used in Hadoop, Spark

---

## 1.3 Data Processing

### Batch Processing
- Processes data in groups/batches
- Scheduled intervals (hourly, daily)
- Examples: ETL jobs, daily reports

### Stream Processing
- Processes data continuously in real-time
- Examples: IoT sensors, click streams

---

# Domain 2: Relational Data on Azure (25-30%)

## 2.1 Azure SQL Database

### Overview
- Fully managed PaaS
- Built on SQL Server engine
- Intelligent performance (auto-tuning)
- 99.99% availability SLA
- Global replication options

### Deployment Tiers
| Tier | Description |
|------|-------------|
| Basic | Low cost, development |
| General Purpose | Balanced |
| Business Critical | High performance, HA |

### Query Examples
```sql
SELECT * FROM customers;
SELECT * FROM orders WHERE amount > 1000;
SELECT o.order_id, c.name FROM orders o
INNER JOIN customers c ON o.customer_id = c.id;
SELECT category, SUM(sales) FROM products GROUP BY category;
```

---

## 2.2 Azure Database for PostgreSQL

- Open-source PostgreSQL
- Single Server and Flexible Server options
- High availability, automatic backups

---

## 2.3 Azure Database for MySQL

- Open-source MySQL
- Single Server tier
- High availability

---

# Domain 3: Non-Relational Data on Azure (20-25%)

## 3.1 Azure Cosmos DB - COMPLETE GUIDE

### Overview
- Globally distributed NoSQL database
- Multi-region replication
- Single-digit millisecond latency (99th percentile)
- Automatic scaling
- 99.999% availability SLA

### Consistency Levels (5 Levels)
| Level | Description |
|-------|-------------|
| Strong | Linearizable, most consistent |
| Bounded Staleness | K versions or T time delayed |
| Session | Consistent within a session |
| Consistent Prefix | No stale reads |
| Eventual | Highest throughput, may be stale |

### Cosmos DB APIs - 5 APIs (VERY IMPORTANT)

#### 1. SQL API (Default)
- Query using SQL syntax
- JSON documents
- Most feature-rich API
- Example:
```sql
SELECT * FROM products WHERE price > 100
```

#### 2. MongoDB API
- Compatible with MongoDB
- Use MongoDB drivers
- Migrate existing MongoDB applications
- 100% MongoDB wire protocol compatibility

#### 3. Cassandra API
- Compatible with Apache Cassandra
- Wide column store model
- Uses CQL (Cassandra Query Language)
- Example CQL:
```sql
CREATE KEYSPACE mykeyspace WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};
CREATE TABLE mykeyspace.users (user_id int PRIMARY KEY, name text, email text);
SELECT * FROM mykeyspace.users WHERE user_id = 1;
```

#### 4. Gremlin API (GRAPH DATABASE - VERY IMPORTANT)
- Graph database API
- Vertices (entities) and Edges (relationships)
- Uses Gremlin traversal language
- Used for: Social networks, Recommendation engines, Fraud detection

**Gremlin Query Examples:**
```gremlin
// Create a vertex (person)
g.addV('person').property('name', 'John').property('age', 30)

// Create vertex with ID
g.addV('person').property(id, '1').property('name', 'John')

// Create edge (knows relationship)
g.V('1').addE('knows').to(g.V('2'))

// Query: Get all vertices
g.V()

// Query: Get vertex by ID
g.V('1')

// Query: Get vertex properties
g.V('1').values()

// Query: Get edges from vertex
g.V('1').outE()

// Query: Get connected vertices
g.V('1').out()

// Query: Filter by property
g.V().has('person', 'age', gt(25))

// Query: Count vertices
g.V().count()

// Query: Get neighbors (friends of friends)
g.V('1').out('knows').out('knows')
```

**Graph Concepts:**
- Vertex (V): Entity like Person, Product, Location
- Edge (E): Relationship between vertices
- Properties: Attributes on vertices/edges
- Label: Type of vertex or edge (e.g., 'person', 'knows')

#### 5. Table API
- Key-value store
- Migrate from Azure Table Storage
- Simple operations using OData protocol

### Partitioning in Cosmos DB
- Data distributed across partitions
- Partition key determines distribution
- Choose partition key carefully for performance
- Logical partitions (unlimited) → Physical partitions (limited)

### Request Units (RUs)
- Throughput currency in Cosmos DB
- Every operation consumes RUs
- RUs depend on: data size, operations performed, consistency level
- Two modes: Provisioned (reserved) or Serverless (pay-per-use)

---

## 3.2 Azure Blob Storage

### Overview
- Object storage for unstructured data
- Three storage tiers

### Storage Tiers (IMPORTANT)
| Tier | Use Case | Minimum Retention |
|------|----------|-------------------|
| Hot | Frequent access | None |
| Cool | Infrequent (30+ days) | 30 days |
| Archive | Rare (180+ days) | 180 days |

### Blob Types
- **Block blobs**: Text, binary files (images, videos)
- **Page blobs**: Random access (VHD files)
- **Append blobs**: Log files

### Use Cases
- Images, videos, documents
- Backups and archives
- Big data analytics (Data Lake)
- CDN content

---

## 3.3 Azure Table Storage

- NoSQL key-value store
- Simple schema
- Fast and cost-effective
- Now migrating to Cosmos DB Table API

---

## 3.4 Azure File Storage

- SMB file shares in cloud
- Compatible with Windows, Linux
- Mount to VMs

---

# Domain 4: Analytics Workload on Azure (25-30%)

## 4.1 Azure Synapse Analytics

### Overview
- Enterprise data warehouse (formerly SQL Data Warehouse)
- Run SQL queries on data at scale
- Serverless and dedicated compute options

### Components

#### SQL Pools
- **Dedicated SQL Pool**: Provisioned compute for predictable workloads
  - Data warehousing units (DWUs) for scaling
  - Materialized views
  - PolyBase for external data

- **Serverless SQL Pool**: Pay-per-query
  - No infrastructure management
  - Query data in Data Lake
  - Serverless endpoint

#### Spark Pools
- Apache Spark for big data processing
- Scala, Python, .NET, SQL
- Delta Lake support
- MLlib for machine learning

#### Data Integration
- Pipelines (like Azure Data Factory)
- Copy data from 90+ connectors
- Data flows for visual ETL

### Use Cases
- Enterprise reporting
- Data warehousing
- Advanced analytics
- Big data processing

---

## 4.2 Azure Databricks

### Overview
- Managed Apache Spark platform
- Collaborative notebooks
- Auto-scaling clusters

### Key Components

#### Notebooks
- Interactive coding environment
- Languages: Python, Scala, SQL, R
- Cell-based execution
- Visualizations

#### Clusters
- **Auto-scaling**: Automatically adjusts based on workload
- **Photon**: Fast Spark engine
- **Delta Lake**: ACID transactions on Spark
- **MLflow**: ML lifecycle management (tracking, models, registry)
- **Unity Catalog**: Data governance and access control

#### Workspace
- Notebooks
- Clusters
- Jobs
- Models
- Experiments

### Use Cases
- Data engineering
- Data science
- Machine learning
- Streaming analytics

---

## 4.3 Azure Stream Analytics

### Overview
- Real-time stream processing
- Fully managed
- Event Hub/IoT Hub integration
- Low latency (milliseconds)

### Windowing Functions (IMPORTANT)

| Window Type | Description |
|-------------|-------------|
| Tumbling | Fixed, non-overlapping windows |
| Hopping | Overlapping by fixed interval |
| Sliding | Based on conditions |
| Session | Groups events by gap |

### Example Queries
```sql
-- Tumbling window (5 minutes)
SELECT System.Timestamp() AS WindowEnd, COUNT(*) AS EventCount
INTO output
FROM input TIMESTAMP BY EventTime
GROUP BY TumblingWindow(minute, 5)

-- Sliding window
SELECT * FROM input
WHERE temperature > Threshold
GROUP BY SlidingWindow(minute, 10)

-- Session window
SELECT * FROM input
GROUP BY SessionWindow(minute, 5, 15)
```

### Input Sources
- Event Hubs
- IoT Hub
- Blob Storage

### Output Destinations
- Blob Storage
- Event Hubs
- SQL Database
- Cosmos DB
- Power BI
- Azure Functions

### Use Cases
- Real-time dashboards
- IoT data processing
- Anomaly detection
- Click stream analytics

---

## 4.4 Azure Data Lake

### Overview
- Scalable data storage for analytics
- Hierarchical namespace (Gen2)
- Massive scale
- Multiple format support

### Data Lake Gen2 Features
- **Hierarchical namespace**: Directories vs flat blob
- **ACLs**: Fine-grained access control (POSIX-like)
- **Security**: Encryption at rest, role-based access
- **Integration**: Works with all Azure analytics services

### Storage Hierarchy
```
datalake/
├── raw/           (Bronze - raw ingested data)
│   └── year=2024/
│       └── month=01/
├── silver/        (Cleaned, transformed)
│   └── customers/
├── gold/          (Business-ready aggregates)
│   └── analytics/
└── models/        (ML models)
```

### Use Cases
- Store any type of data
- Big data analytics
- Data warehousing landing zone
- Raw data storage (Bronze/Silver/Gold pattern)

---

## 4.5 Power BI - COMPLETE GUIDE

### Overview
- Business analytics service by Microsoft
- Visualizations and dashboards
- Connect to many data sources
- Self-service BI

### Power BI Components

#### Power BI Desktop
- Windows application
- Create reports and visualizations
- Publish to Power BI Service

#### Power BI Service (powerbi.com)
- Cloud-based
- Share reports and dashboards
- Scheduled refresh
- Collaboration

#### Power BI Mobile
- iOS and Android apps
- View reports on mobile

### Building Blocks

#### Datasets
- Data source connections
- Can be imported or DirectQuery
- Refresh schedules

#### Reports
- Collection of visualizations on pages
- Interactive - cross-filtering
- Multiple pages

#### Dashboards
- Single-page collection of tiles
- Real-time tiles
- Mobile-optimized

#### Workspaces
- Collaboration spaces
- App workspaces for distribution

### Visualization Types
| Type | Use Case |
|------|----------|
| Table | Detailed data |
| Matrix | Cross-tab with hierarchies |
| Bar/Column | Comparisons |
| Line/Area | Trends over time |
| Pie/Donut | Part-to-whole |
| Map | Geographic data |
| Scatter | Correlation |
| KPI | Target vs actual |
| Gauge | Performance meter |
| Ribbon | Rank changes |

### Data Sources (100+ connectors)
- Excel, CSV, XML
- Azure SQL, Cosmos DB
- SharePoint, OneDrive
- Web APIs
- SQL Server, Oracle
- And many more...

### Key Concepts

#### DAX (Data Analysis Expressions)
- Formula language for calculations
- Measures and calculated columns
- Example:
```dax
Total Sales = SUM(Sales[Amount])
Sales YoY = CALCULATE(SUM(Sales[Amount]), SAMEPERIODLASTYEAR(Date[Date]))
```

#### Relationships
- Connect tables
- Cardinality: One-to-One, One-to-Many, Many-to-Many
- Cross-filter direction

#### Row-Level Security (RLS)
- Restrict data by user
- Role-based filtering
- Test in Desktop

### Use Cases
- Self-service BI
- Embedded analytics
- Real-time dashboards
- Enterprise reporting

### Integration with Azure
- Connect to Azure SQL, Cosmos DB, Data Lake
- Power BI Embedded for custom apps
- Paginated reports for printing

---

## 4.6 Azure Data Factory (Mentioned in Analytics)

### Overview
- ETL/ELT service
- Data integration pipelines
- 90+ connectors

### Key Components
- **Pipelines**: Workflow of activities
- **Activities**: Copy, transform, control
- **Datasets**: Data structures
- **Linked Services**: Connections
- **Triggers**: Schedule/pevent-based execution

### Integration with Analytics
- Copy data to Data Lake
- Transform with Data Flows
- Orchestrate Synapse/Databricks

---

# Quick Summary - What to Focus

## MUST KNOW:

### Cosmos DB
- 5 APIs: SQL, MongoDB, Cassandra, Gremlin (Graph), Table
- Consistency levels (5 types)
- Request Units (RUs)
- Partition keys
- 99.999% availability

### Gremlin (Graph)
- Vertices and Edges
- Basic traversal queries
- Use cases: Social networks, fraud detection

### Power BI
- Building blocks: Datasets, Reports, Dashboards
- Visualization types
- DAX basics
- Integration with Azure services

### Blob Storage
- Tiers: Hot, Cool, Archive
- Use cases for each tier

### Analytics Services
- Synapse: SQL + Spark + Pipelines
- Databricks: Spark, Notebooks, ML
- Stream Analytics: Real-time, Windowing

---

# Exam Tips

1. Know ALL 5 Cosmos DB APIs - especially Gremlin for graph
2. Blob storage tiers - know when to use each
3. Power BI is for visualization, not storage/processing
4. Synapse = Enterprise DW, Databricks = Spark/ML
5. Stream Analytics = Real-time processing
6. Basic SQL queries are essential
7. Consistency levels in Cosmos DB
8. Gremlin queries for graph data
