# 01 - Core Data Concepts (DP-900)

## Learning Goals

By the end of this tutorial, you should be able to:

- Differentiate structured, semi-structured, and unstructured data
- Select a suitable storage format for a scenario
- Explain OLTP vs OLAP workloads
- Identify key responsibilities of DBA, Data Engineer, and Data Analyst

---

## 1.1 Understanding Data Representation

### Structured Data

Structured data follows a rigid, predefined schema where every record contains the same fields in the same format. Think of it like a well-organized spreadsheet where each column has a specific data type and every row follows the exact same structure.

**Example:**

| CustomerId | Name  | City     |
|------------|-------|----------|
| 1001       | Ravi  | Seattle  |
| 1002       | Meera | New York |

**Typical use cases:**
- Relational databases
- Data warehouses

**Why it matters:**
- Easy to validate and query with SQL
- Best when business rules are strict
- Strong data integrity through constraints
- Enables complex joins and transactions

**Real-world example:**
Banks use structured data for account records because the strict schema ensures every transaction has the required fields and maintains accuracy. Each customer record has a unique CustomerId, and every transaction links to that customer through a foreign key relationship.

---

### Semi-Structured Data

Semi-structured data has organizational properties but lacks the rigid row-column format of structured data. JSON and XML documents are perfect examples—you can have nested objects, arrays, and varying fields between records without breaking the format.

**Example JSON:**

```json
{
  "orderId": 5001,
  "customer": "Nina",
  "items": [
    {"sku": "A10", "qty": 2},
    {"sku": "B50", "qty": 1}
  ]
}
```

Notice that:
- One order might include shipping details while another omits them
- The "items" array can contain any number of products
- Each item can have different fields as needed

**Typical use cases:**
- Document databases (Azure Cosmos DB, MongoDB)
- Data lakes for storing raw event data
- Message and event payloads from APIs

**Why it matters:**
- Flexible for changing data fields without schema migrations
- Good for APIs, logs, and app events
- Modern applications often communicate via JSON
- Schema can evolve over time without downtime

**Real-world example:**
An e-commerce product catalog might have different attributes for different product types—a T-shirt has size and color, while a laptop has processor and RAM specifications. Document databases accommodate this flexibility naturally.

---

### Unstructured Data

Unstructured data has no predefined model or organization—it includes everything from text documents and images to audio recordings and video files. This represents the fastest-growing category of data in modern organizations, accounting for approximately 80% of enterprise data according to industry estimates.

**Examples:**
- PDF files and Word documents
- Images and photographs
- Video files and recordings
- Audio clips and voice memos
- Email bodies and chat messages
- Social media posts

**Typical use cases:**
- Object storage such as Azure Blob Storage
- Content management systems
- Media and entertainment platforms

**Why it matters:**
- Largest growth area in modern systems
- Usually paired with metadata for search and analytics
- Requires different processing approaches than tabular data
- Often requires AI/ML for meaningful analysis

**Real-world example:**
A healthcare organization stores medical imaging (X-rays, MRIs, CT scans) as unstructured data. While the images themselves have no inherent structure, they're tagged with metadata like patient ID, date, imaging type, and body part—which enables searching and organization.

---

### Key Distinction: Schema-on-Write vs Schema-on-Read

**Schema-on-write** (used by structured data):
- Schema is enforced when data is written
- Invalid data is rejected at insertion time
- Provides strong data quality guarantees
- Example: SQL databases

**Schema-on-read** (used by semi-structured and unstructured data):
- Schema is defined when data is read
- Flexibility to store diverse data formats
- Data quality must be enforced at application level
- Example: Data lakes, document databases

**Exam tip:** The DP-900 exam tests your ability to match data types to appropriate storage solutions. Remember that JSON is semi-structured (not unstructured) because it has organizational properties even without rigid schema.

---

## 1.2 Understanding Data Storage Options

### File Formats

Choosing the right file format significantly impacts performance, storage costs, and interoperability.

#### CSV / TSV

- **What it is:** Simple text format with comma or tab delimiters
- **Characteristics:**
  - Human-readable and easy to generate
  - No built-in schema enforcement
  - No compression support
  - Works with virtually every tool

- **Use when:**
  - Data exchange between different systems
  - Initial data exploration
  - Small to medium datasets
  - Simple data exports

- **Example:**
  ```csv
  CustomerId,Name,City
  1001,Ravi,Seattle
  1002,Meera,New York
  ```

---

#### JSON / XML

- **What it is:** Hierarchical, self-describing data formats
- **Characteristics:**
  - Supports nested structures and arrays
  - Self-describing—includes field names
  - Human-readable
  - Wide tool support

- **Use when:**
  - Web API payloads
  - Application configuration
  - Event data and log files
  - Semi-structured data storage

- **Example JSON:**
  ```json
  {
    "customer": {
      "name": "Ravi",
      "orders": [
        {"id": 1, "total": 150.00}
      ]
    }
  }
  ```

---

#### Parquet / ORC / Avro

- **What they are:** Columnar formats optimized for analytical workloads
- **Characteristics:**
  - Columnar storage (stores data by column, not row)
  - Excellent compression ratios
  - Built-in schema support
  - Optimized for analytics queries

- **Use when:**
  - Large analytical workloads
  - Data lake processing
  - Spark and big data workflows
  - When you need to read specific columns efficiently

- **Why Parquet is popular for analytics:**
  - Only reads columns needed for the query
  - Compression reduces storage costs
  - Schema evolution support
  - Native support in Azure Data Lake, Databricks, Synapse

**Exam tip:** For the DP-900, remember that columnar formats like Parquet are best for analytical workloads while CSV/JSON are better for data exchange and flexible storage.

---

### Database Categories

#### Relational Databases

- **Structure:** Table-based with rows and columns
- **Key features:**
  - Primary keys and foreign keys
  - Constraints for data integrity
  - SQL query language
  - ACID transaction support

- **Best for:**
  - Applications requiring strong consistency
  - Complex joins and relationships
  - Transactional workloads (OLTP)
  - Structured data with fixed schemas

- **Examples:** Azure SQL Database, MySQL, PostgreSQL, SQL Server

---

#### Non-Relational Databases

NoSQL databases sacrifice some relational features for scalability and flexibility:

- **Key-value stores:** Fast lookups by key
  - Example: Redis, Azure Table Storage
  - Use for: Session data, user profiles, caching

- **Document databases:** Flexible JSON-like documents
  - Example: MongoDB, Azure Cosmos DB
  - Use for: Catalogs, content management, evolving schemas

- **Column-family databases:** Wide-column storage
  - Example: Cassandra, Azure Cosmos DB (Cassandra API)
  - Use for: Time-series data, event logging, massive scale

- **Graph databases:** Relationship-first data model
  - Example: Neo4j, Azure Cosmos DB (Gremlin API)
  - Use for: Social networks, fraud detection, recommendations

---

### Choosing a Storage Option (Simple Rules)

1. **Need strong transactions and joins?** → Use relational database
2. **Need flexible schema and global scale?** → Use non-relational database
3. **Need cheap large file storage?** → Use object/file storage
4. **Need analytical queries on large datasets?** → Use data warehouse or lake
5. **Need to store diverse data types in raw form?** → Use data lake

---

## 1.3 Understanding Data Workloads

### OLTP (Online Transaction Processing)

OLTP systems handle the day-to-day operational activities of businesses.

**Characteristics:**
- Many small, frequent operations
- Fast reads and writes
- High concurrency (many simultaneous users)
- Low latency requirements (milliseconds)
- Strong data consistency required

**Real-world examples:**
- E-commerce checkout processing
- ATM cash withdrawal requests
- Airline ticket booking
- Payment processing
- Inventory updates

**Design priorities:**
- **Low latency:** Users expect instant responses
- **Data integrity:** Every transaction must be accurate
- **Reliable transactions (ACID):**
  - Atomicity: Complete entirely or not at all
  - Consistency: Maintain valid database state
  - Isolation: Concurrent transactions don't interfere
  - Durability: Committed data survives failures

**Typical operations:**
- Single record inserts, updates, deletes
- Point queries by primary key
- Simple aggregations

---

### OLAP (Online Analytical Processing)

OLAP systems support decision-making through complex queries that analyze historical data.

**Characteristics:**
- Large scans and aggregations
- Historical and trend analysis
- Fewer write operations than OLTP
- Query latency measured in seconds to minutes
- Large data volume per query

**Real-world examples:**
- Monthly sales dashboard
- Profitability analysis across product lines
- Customer segmentation for marketing
- Risk assessment reports
- Supply chain optimization

**Design priorities:**
- **Query throughput:** Handle many concurrent analytical queries
- **Efficient aggregation:** Calculate sums, averages, counts quickly
- **Data model for analysis:** Star schemas, denormalized designs

**Typical operations:**
- Full table scans
- Complex joins across multiple large tables
- Grouping, aggregation, and window functions

---

### OLTP vs OLAP Quick Comparison

| Area | OLTP | OLAP |
|------|------|------|
| **Purpose** | Run business operations | Analyze business data |
| **Data volume per query** | Small (single records) | Large (millions of rows) |
| **Query type** | Insert/Update/Select by key | Aggregate/Group/Join |
| **Latency** | Milliseconds | Seconds to minutes |
| **Data freshness** | Near real-time | Periodic or near real-time |
| **Users** | Many concurrent (thousands) | Few concurrent (dozens) |
| **Design focus** | Transaction integrity | Query performance |
| **Schema** | Highly normalized | Often denormalized |

---

### How OLTP and OLAP Work Together

Modern enterprises use both systems in a data architecture:

1. **Operational systems** (OLTP) handle day-to-day transactions
2. **ETL/ELT pipelines** extract data from OLTP systems
3. **Data warehouse** (OLAP) stores curated analytical data
4. **BI tools** query the warehouse for reports and dashboards

This separation allows each system to optimize for its specific workload—OLTP for transaction speed, OLAP for query performance.

---

## 1.4 Understanding Data Roles and Responsibilities

### Database Administrator (DBA)

The DBA is responsible for the operational health of data platforms.

**Typical responsibilities:**
- **Backup and recovery:** Configure backup schedules, test restore procedures, manage disaster recovery
- **Security and access:** Manage user accounts, permissions, encryption, audit logging
- **Performance monitoring:** Track query performance, optimize indexes, manage capacity
- **Availability:** Configure high availability, replication, failover
- **Patching and updates:** Apply database engine updates and security patches
- **Storage management:** Monitor storage consumption, plan capacity growth

**Tools used:** SQL Server Management Studio, Azure Portal, monitoring dashboards

---

### Data Engineer

Data Engineers build the infrastructure that moves and transforms data.

**Typical responsibilities:**
- **Pipeline development:** Create ingestion pipelines from source systems to storage
- **Data transformation:** Clean, reshape, and enrich data for analytical use
- **Data modeling:** Design analytical schemas (star schemas, snowflake schemas)
- **Orchestration:** Schedule and monitor data flows (nightly batches, real-time streams)
- **Data quality:** Implement validation and quality checks
- **Tool selection:** Choose appropriate Azure services for data workloads

**Tools used:** Azure Data Factory, Azure Databricks, Azure Synapse Analytics, Python, Spark

---

### Data Analyst

Data Analysts bridge the gap between data and business decisions.

**Typical responsibilities:**
- **Data exploration:** Understand available datasets and their meanings
- **Report building:** Create reports and dashboards using BI tools
- **Metric definition:** Work with business stakeholders to define KPIs
- **Ad-hoc analysis:** Answer specific business questions
- **Insight communication:** Present findings in accessible ways

**Tools used:** Power BI, Excel, SQL, Tableau, visualization tools

---

### Role Boundaries Summary

| Role | Primary Focus | Owns |
|------|---------------|------|
| DBA | Operational health | Reliability, security, availability of data platforms |
| Data Engineer | Data movement | Pipelines, transformations, data infrastructure |
| Data Analyst | Business insights | Reports, dashboards, analytical queries |

**Note:** In small teams, one person often performs multiple roles. The key is understanding the different skill sets each role requires.

---

## Mini Practice Tasks

### Task 1: Classify Data Type

Identify whether each is structured, semi-structured, or unstructured:

1. Customer table in SQL database with fixed columns
2. Product catalog JSON from API with varying attributes
3. Recorded support call audio files
4. Website clickstream log files
5. Employee XML documents with flexible fields

**Answers:**
1. Structured
2. Semi-structured
3. Unstructured
4. Semi-structured
5. Semi-structured

---

### Task 2: Identify Workload Type

Identify whether each scenario is OLTP or OLAP:

1. Fraud detection dashboard analyzing 2 years of transaction data
2. ATM cash withdrawal request
3. Customer placing an order on website
4. Monthly sales report by region
5. Real-time inventory count update

**Answers:**
1. OLAP
2. OLTP
3. OLTP
4. OLAP
5. OLTP

---

### Task 3: Match Role to Task

Identify which role (DBA, Data Engineer, Data Analyst) performs each task:

1. Building a nightly ingestion pipeline from CRM to data lake
2. Configuring geo-replication for disaster recovery
3. Creating a sales dashboard for executives
4. Optimizing slow-running queries
5. Defining customer lifetime value metric

**Answers:**
1. Data Engineer
2. DBA
3. Data Analyst
4. DBA / Data Engineer
5. Data Analyst

---

## Quick Self-Check Questions

Test your understanding with these questions:

1. **Can you explain the difference between schema-on-write and schema-on-read?**
   - Schema-on-write enforces structure when data enters the system
   - Schema-on-read defines structure when data is read

2. **Can you justify when to use Parquet instead of CSV?**
   - Parquet for large analytical workloads (columnar, compressed)
   - CSV for data exchange and simple scenarios

3. **Can you identify OLTP vs OLAP from a scenario in one sentence?**
   - OLTP: "Processing a customer purchase"
   - OLAP: "Analyzing last year's sales trends"

---

## Common Mistakes to Avoid

1. **Assuming JSON is always unstructured:** JSON is semi-structured because it has organizational properties
2. **Assuming all analytics starts with relational tables:** Data lakes store raw data that feeds warehouses
3. **Confusing OLTP and OLAP:** Remember—transactions (OLTP) vs analysis (OLAP)
4. **Choosing the wrong storage format:** Match format to use case, not personal preference
