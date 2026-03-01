# 04 - Analytics Workload (DP-900)

## Learning Goals

By the end of this tutorial, you should be able to:

- Explain the parts of a modern analytics architecture
- Compare batch and streaming approaches
- Choose between warehouse, lake, and lakehouse patterns
- Describe Power BI core modeling and visualization concepts

---

## 4.1 Large-Scale Analytics Elements

### End-to-End Analytics Pipeline

A modern analytics system moves data from operational sources through processing stages to deliver business insights. Understanding each stage helps you design appropriate solutions.

#### Typical Analytics Flow

1. **Ingest data** from apps, databases, files, and devices
   - Sources: Transaction databases, IoT sensors, web applications, external APIs
   - Methods: Batch files, streaming events, CDC (Change Data Capture)

2. **Store raw data** in scalable storage
   - Usually a data lake for flexibility
   - Keep original format for reprocessing if needed

3. **Transform and clean data**
   - Remove duplicates
   - Handle missing values
   - Standardize formats
   - Apply business logic

4. **Model data** for analysis
   - Create dimensional models
   - Build aggregations
   - Optimize for query performance

5. **Build reports and dashboards**
   - Create visualizations
   - Enable self-service analytics
   - Distribute to stakeholders

---

### Ingestion Patterns

Choosing between batch and streaming ingestion depends on business requirements for latency, complexity, and cost.

#### Batch Ingestion

**How it works:**
- Data arrives in scheduled intervals (hourly, daily, weekly)
- Files accumulate and get processed in chunks
- Traditional approach to data integration

**Characteristics:**
| Aspect | Description |
|--------|-------------|
| Latency | Minutes to hours delay |
| Complexity | Lower operational complexity |
| Cost | Generally lower |
| Reliability | Easier to ensure |
| Use case | Daily reports, standard analytics |

**Examples:**
- Nightly batch import of sales data
- Hourly file transfers from partner systems
- Daily CRM data sync

**When to use batch:**
- Data freshness of hours/days is acceptable
- Budget or complexity constraints
- Standard reporting and dashboards
- When you can schedule around batch windows

---

#### Streaming Ingestion

**How it works:**
- Data arrives continuously as events
- Processed in near real-time
- Results available within seconds/minutes

**Characteristics:**
| Aspect | Description |
|--------|-------------|
| Latency | Seconds to sub-seconds |
| Complexity | Higher (state management, exactly-once) |
| Cost | Higher infrastructure |
| Reliability | More complex guarantees |
| Use case | Real-time dashboards, alerts |

**Examples:**
- IoT sensor readings processed as they arrive
- Clickstream analytics for real-time personalization
- Fraud detection during transactions
- Live operational dashboards

**When to use streaming:**
- Need seconds-level latency
- Real-time decision making
- IoT and time-series scenarios
- When historical analysis also needed (can store raw for batch too)

---

### ETL vs ELT

The sequence of operations in your data pipeline affects flexibility, performance, and tooling.

#### ETL (Extract, Transform, Load)

**Traditional approach:**
1. Extract data from sources
2. Transform data in staging area
3. Load into target warehouse

**Characteristics:**
- Transform happens before loading
- Target system receives clean, ready-to-query data
- Legacy approach, still valid in many scenarios
- Transformation logic in pipeline tools (Data Factory, SSIS)

**Advantages:**
- Clean data in warehouse from start
- Less transformation work in warehouse
- Sensitive data filtered before reaching warehouse

**Disadvantages:**
- Can't re-transform once loaded
- Requires knowing transformation requirements upfront
- Pipeline tools may have limited transformation capabilities

---

#### ELT (Extract, Load, Transform)

**Modern approach:**
1. Extract data from sources
2. Load raw data into target
3. Transform using target platform capabilities

**Characteristics:**
- Raw data loads first
- Transformation happens in warehouse
- Leverages powerful compute in target platform

**Advantages:**
- Can re-transform as requirements change
- Leverage warehouse's powerful processing
- Simpler pipeline (just extract and load)
- Schema-on-read flexibility

**Disadvantages:**
- Requires warehouse with transformation capabilities
- Raw data sits in warehouse until transformed

**Why ELT is popular in cloud:**
- Cloud data warehouses (Synapse, Snowflake, BigQuery) have massive parallel processing
- Pay for compute only when transforming
- Can handle any data size

---

### Analytical Data Store Options

Choosing the right storage pattern depends on data types, query patterns, and organizational needs.

#### Data Warehouse

**What it is:** A purpose-built analytical database that stores structured data in a curated, optimized format for complex queries and reporting.

**Key characteristics:**
- Structured data only (tables with defined schemas)
- Highly optimized for analytical queries
- Typically uses dimensional modeling (star schema)
- Supports complex SQL queries efficiently

**Architecture:**
```
Source Systems → ETL → Staging → Data Warehouse → BI Tools
                         ↑
                    Clean, conformed,
                    integrated data
```

**Best for:**
- Standard enterprise reporting
- Complex analytical queries with joins and aggregations
- When data is well-structured and predictable
- Organizations with established BI practices

**Azure services:**
- Azure Synapse Analytics (formerly SQL DW)
- Azure SQL Database (for smaller workloads)
- Snowflake, Amazon Redshift

**Example:**
Retail warehouse with fact tables for sales, inventory and dimension tables for products, customers, stores. Analysts query using SQL to answer: "What were total sales by region last quarter?"

---

#### Data Lake

**What it is:** A centralized repository that stores all data at any scale. Data is stored in its raw, native format without requiring predefined schemas.

**Key characteristics:**
- Store any data type: structured, semi-structured, unstructured
- Schema-on-read (interpret when reading, not when storing)
- Cost-effective for massive datasets
- Supports diverse workloads (analytics, ML, streaming)

**Architecture:**
```
Source Systems → Ingest → Data Lake → Process → Various Outputs
                                              ↓
                              Analytics | ML | Streaming | Archive
```

**Data formats:**
- Raw files: CSV, JSON, XML
- Optimized formats: Parquet, ORC, Avro
- Delta Lake for ACID transactions on files

**Best for:**
- Exploratory analytics and data science
- Storing diverse data types
- Cost-effective large-scale storage
- Machine learning workflows
- When schema is unknown or changing

**Azure services:**
- Azure Data Lake Storage (ADLS Gen2)
- Amazon S3
- Google Cloud Storage

**Example:**
A company stores website clickstream logs, social media data, product images, and transaction data all in one place. Data scientists explore this data using Spark and Databricks, building ML models without needing to define schemas upfront.

---

#### Lakehouse

**What it is:** An architecture that combines the best of data lakes and data warehouses—the flexibility of data lakes with the management and performance features of data warehouses.

**Key characteristics:**
- ACID transactions on data lake storage
- Support for diverse data types
- Schema enforcement and evolution
- Unified workloads: data engineering + BI

**Architecture:**
```
Data Lake (raw files)
       ↓
Delta Lake / Iceberg (transaction layer)
       ↓
Unified Platform (engineering + BI)
```

**Best for:**
- Organizations wanting both flexibility and governance
- When same data serves ML and BI
- Need ACID guarantees on lake data
- Modern data platform initiatives

**Azure services:**
- Microsoft Fabric (OneLake)
- Databricks (Unity Catalog)

**Example:**
A company stores raw event data in data lake format. Using Delta Lake, they get ACID transactions, time travel, and schema enforcement. The same data serves data engineers building pipelines and analysts running BI reports—no separate warehouse needed.

---

### Service Landscape (DP-900 Context)

#### Azure Databricks

**What it is:** A collaborative Apache Spark-based analytics platform for big data and AI.

**Key features:**
- Managed Spark environment
- Notebook-based collaboration
- Delta Lake support
- MLflow for machine learning lifecycle
- Integration with Azure Data Lake and Synapse

**Use cases:**
- Data engineering pipelines
- Data science and ML
- Streaming analytics
- Ad-hoc exploration

---

#### Microsoft Fabric

**What it is:** An end-to-end analytics platform that unifies data movement, data engineering, data warehousing, and business intelligence.

**Key features:**
- OneLake (unified storage)
- Data Factory (pipelines)
- Synapse (analytics)
- Power BI (visualization)
- Real-time analytics

**Use cases:**
- Unified analytics platform
- End-to-end data solutions
- Self-service BI

---

#### Related Services

**Azure Synapse Analytics:**
- Enterprise data warehouse
- Spark pools for big data processing
- Pipeline orchestration
- Near real-time analytics

**Azure Data Factory:**
- Data integration service
- Pipeline orchestration
- Hybrid data movement
- 90+ connectors

---

### Exam Focus

For the DP-900 exam, remember:

- **Understand what each architecture solves:** Warehouse for curated analytics, lake for flexible exploration, lakehouse for both
- **Know that modern systems frequently combine multiple services:** Many solutions use lake for raw data, warehouse for curated data
- **Batch vs streaming:** Choose based on latency requirements, not just because streaming is "newer"

---

## 4.2 Real-Time Analytics

### Batch vs Streaming Quick Comparison

| Area | Batch | Streaming |
|------|-------|-----------|
| **Data arrival** | Scheduled chunks | Continuous events |
| **Latency** | Minutes/hours | Seconds/sub-seconds |
| **Complexity** | Lower | Higher |
| **Infrastructure** | Simpler | More components |
| **Typical use** | Daily reports | Live alerts, dashboards |
| **Cost** | Lower | Higher |

---

### Real-Time Processing Pattern

#### Step-by-Step Flow

1. **Capture events**
   - Sources: IoT devices, web clicks, transactions
   - Service: Event Hubs, IoT Hub
   - Format: JSON, Avro

2. **Process/window/aggregate events**
   - Filter: Remove unwanted events
   - Transform: Enrich, convert formats
   - Window: Aggregate over time windows (tumbling, sliding)
   - Service: Stream Analytics, Spark Structured Streaming

3. **Write results to serving store**
   - Time-series database: Azure Data Explorer
   - Streaming database: Cosmos DB
   - Cache: Redis
   - Warehouse: Synapse/Fabric

4. **Visualize and trigger alerts**
   - Power BI real-time dashboards
   - Azure Monitor alerts
   - Custom applications

---

#### Common Azure Components

**Event ingestion:**
- **Azure Event Hubs:** High-throughput event streaming (millions events/sec)
- **IoT Hub:** Specialized for IoT device communication

**Stream processing:**
- **Azure Stream Analytics:** SQL-like queries, easy to start
- **Spark Structured Streaming (Databricks):** Complex processing, ML integration

**Analytics stores:**
- **Azure Synapse Analytics:** Batch + streaming
- **Microsoft Fabric:** Unified platform
- **Azure Data Explorer (KQL):** Time-series, log analytics

**Visualization:**
- **Power BI:** Real-time dashboards
- **Azure Monitor:** Infrastructure monitoring

---

### Common Real-Time Scenarios

#### Fraud Detection
- Capture: Transaction events from payment systems
- Process: Check against rules, score with ML model
- Output: Block transaction if fraud probability high
- Latency: Sub-second decisions

#### Fleet Monitoring
- Capture: GPS, fuel, engine sensors from vehicles
- Process: Track location, alert on anomalies
- Output: Dashboard showing fleet status
- Latency: Seconds for dashboard, immediate for alerts

#### Website Activity Dashboards
- Capture: Page views, clicks, searches
- Process: Aggregate by user, session, page
- Output: Real-time dashboard showing active users, popular content
- Latency: Seconds

#### Manufacturing Sensor Alerts
- Capture: Temperature, pressure, vibration sensors
- Process: Check against thresholds, detect patterns
- Output: Immediate alerts when thresholds exceeded
- Latency: Milliseconds for alerts

---

## 4.3 Data Visualization with Power BI

### Power BI Building Blocks

Power BI provides a complete suite for data visualization and business intelligence.

#### Dataset (Semantic Model)

The dataset is the analytical foundation—a collection of tables with relationships that defines how data connects.

**Key characteristics:**
- In-memory analytical engine
- Optimized for DAX calculations
- Stores data efficiently with compression
- Enables fast interactive visuals

**Best practice:** Build star schemas with fact and dimension tables for optimal performance and simplicity.

---

#### Report

A report is a multi-page canvas containing visualizations that work together.

**Key characteristics:**
- Multiple pages (like Excel worksheets)
- Cross-filtering between visuals
- Interactive (click to filter)
- Can be shared or embedded

---

#### Dashboard

A dashboard is a single-page view optimized for monitoring.

**Key characteristics:**
- One-page summary
- Pinned visuals from one or more reports
- Tiles update on refresh
- Good for executive summaries

---

#### Workspace

A workspace is a collaboration boundary for managing content.

**Key characteristics:**
- Contains datasets, reports, dashboards
- Controls who can access content
- Enables shared development
- Supports deployment pipelines (dev/test/prod)

---

### Data Modeling Basics

#### Relationships

Relationships connect tables and determine how filters propagate.

**One-to-many (most common):**
- One record in dimension table relates to many in fact table
- Example: One customer → Many orders
- Visualized with "*" on the many side

**Relationship direction:**
- Filters flow from "one" side to "many" side
- Direction matters for correct calculations
- Bidirectional filtering available but use carefully

**Example model:**
```
DimCustomer (One) ←→ FactSales (Many)
- CustomerKey (PK)    - SalesKey (PK)
- CustomerName        - CustomerKey (FK)
- City                - ProductKey (FK)
- Country             - Amount
                      - Date
```

---

#### Measures vs Calculated Columns

**Measures:**
- Calculated at query time based on filter context
- Don't add data to model
- Recalculate whenever used
- Usually preferred for aggregations

**Example measure:**
```DAX
Total Sales = SUM(Sales[Amount])
```
- Returns sum of Amount column
- Changes based on filters (year, region, etc.)

---

**Calculated Columns:**
- Computed when data loads
- Stored in model
- Fixed value per row
- Use when you need row-level values

**Example calculated column:**
```DAX
Full Name = Customer[FirstName] & " " & Customer[LastName]
```
- Concatenates first and last name
- Stored as single column
- Doesn't change based on filters

---

**When to use each:**

| Use Measure | Use Calculated Column |
|-------------|----------------------|
| Aggregations (sum, count, average) | Row-level math (quantity × price) |
| Percentages and ratios | Text combinations |
| Complex time intelligence | Conditional values that don't aggregate |
| When value should change with filters | When value is constant per row |

---

### Choose the Right Visual

Selecting appropriate visualizations makes reports effective. Power BI offers many visualization types, each designed for specific analytical purposes.

#### Basic Chart Types

##### Line Chart
- **Best for:** Showing trends over time
- **How it works:** Connects data points with a line
- **Example use:** Monthly sales over the past year, website traffic trends
- **Tips:** Use for 3+ time periods to show clear trend direction

##### Area Chart
- **Best for:** Showing volume over time with emphasis on total
- **How it works:** Like line chart but filled below the line
- **Example use:** Revenue accumulation over time, total storage usage
- **Tips:** Good for showing part-to-whole over time

##### Bar Chart (Horizontal)
- **Best for:** Comparing categories, especially with long labels or many categories
- **How it works:** Horizontal bars represent values
- **Example use:** Sales by product name, countries by population
- **Tips:** Easiest to read when sorted largest to smallest

##### Column Chart (Vertical)
- **Best for:** Comparing values across categories with short labels
- **How it works:** Vertical columns represent values
- **Example use:** Quarterly revenue, sales by region
- **Tips:** Best with 2-10 categories

##### Stacked Bar Chart
- **Best for:** Showing total and its parts across categories
- **How it works:** Bars divided into segments showing contribution
- **Example use:** Sales by region split by product category
- **Tips:** Use when you want both total comparison and composition

##### Pie Chart
- **Best for:** Showing part-to-whole with few categories (2-5)
- **How it works:** Circle divided into proportional slices
- **Example use:** Market share, budget allocation
- **Warning:** Avoid with many categories—hard to read slices!
- **Tips:** Consider stacked bar instead for easier comparison

---

#### Distribution Charts

##### Histogram
- **Best for:** Showing how values distribute across ranges
- **How it works:** Bars represent frequency in value ranges (bins)
- **Example use:** Customer age distribution, order value ranges
- **Tips:** Choose appropriate bin size for your data

##### Box Plot
- **Best for:** Showing statistical distribution (median, quartiles, outliers)
- **How it works:** Box shows Q1-Q3 range, line shows median, dots show outliers
- **Example use:** Salary distributions, test score ranges
- **Tips:** Great for comparing distributions across categories

##### Scatter Plot
- **Best for:** Showing relationship between two numeric values
- **How it works:** Each point is one record, positioned by X and Y values
- **Example use:** Revenue vs advertising spend, height vs weight
- **Tips:** Add trendline to show correlation clearly

---

#### Comparison Charts

##### Treemap
- **Best for:** Showing hierarchical data as nested rectangles
- **How it works:** Rectangle size represents value, color can show second dimension
- **Example use:** Sales by category and subcategory
- **Tips:** Good for large datasets where bar charts get too long

##### Funnel Chart
- **Best for:** Showing progression through stages with decreasing values
- **How it works:** Bars narrow at each stage like a funnel
- **Example use:** Sales pipeline, website conversion funnel
- **Tips:** Clearly label the drop-off between stages

##### Gauge Chart
- **Best for:** Showing progress toward a target
- **How it works:** Needle or bar shows current value against min/max/target
- **Example use:** KPI progress, sales target achievement
- **Tips:** Use one gauge per KPI, not multiple on one chart

---

#### Detail and Text Charts

##### Table
- **Best for:** Showing exact values, detailed data
- **How it works:** Rows and columns of data
- **Example use:** Detailed transaction list, top 20 customers
- **Tips:** Sort by most important column, consider conditional formatting

##### Matrix
- **Best for:** Cross-tabulation with aggregations
- **How it works:** Like pivot table with totals
- **Example use:** Sales by region and product category
- **Tips:** Enable column/row subtotals for better analysis

##### Card
- **Best for:** Single important metric (KPI)
- **How it works:** Large number display
- **Example use:** Total revenue, number of customers, conversion rate
- **Tips:** Add trend indicator (up/down arrow) for context

---

#### Mapping and Location Charts

##### Map
- **Best for:** Geographic data visualization
- **How it works:** Data points plotted on geographic background
- **Example use:** Sales by country, customer locations
- **Tips:** Need latitude/longitude or geographic hierarchy

##### Filled Map (Choropleth)
- **Best for:** Showing values by geographic region
- **How it works:** Regions colored by value intensity
- **Example use:** Sales by state, population by country
- **Tips:** Use for comparison, not exact values

---

#### When to Use Each Visual

| Insight You Want | Recommended Visual |
|-----------------|-------------------|
| Trend over time | Line chart, Area chart |
| Compare categories | Bar chart, Column chart |
| Show composition | Stacked bar, Pie (few categories) |
| Show total + parts | Stacked bar, Treemap |
| Distribution | Histogram, Box plot |
| Relationship between values | Scatter plot |
| Progression through stages | Funnel chart |
| Progress toward goal | Gauge, Card |
| Exact detailed values | Table, Matrix |
| Geographic analysis | Map, Filled Map |
| Single KPI snapshot | Card, Gauge |

---

#### Visual Design Best Practices

1. **Keep it simple:** Each visual should tell one story
2. **Use color intentionally:** Highlight key data, don't overuse
3. **Label clearly:** Titles, axis labels, legends
4. **Sort meaningfully:** Alphabetical is rarely the best choice
5. **Consider accessibility:** Use patterns in addition to color
6. **Match visual to data type:** Don't use line charts for categories

---

### Sharing and Governance Basics

#### Publish and Share
1. Publish reports to workspaces
2. Share workspace or individual reports
3. Export to PDF/PPT if needed
4. Embed in applications (pro tier)

#### Access Control
- Workspace roles: Admin, Member, Contributor, Viewer
- Build sharing into report design with row-level security (RLS)
- Use Azure AD for authentication

#### Refresh Management
- Configure scheduled refresh (daily, hourly)
- Ensure data source credentials are current
- Monitor refresh history for failures

---

## End-to-End Scenario Example

### Scenario

A retail company collects:
- Point-of-sale (POS) transactions from stores
- Website clickstream data
- Inventory updates from warehouses

### Possible Design

1. **Ingestion:**
   - POS: Batch (nightly files from stores)
   - Clicks: Streaming (real-time from website)
   - Inventory: Batch (hourly from ERP)

2. **Storage:**
   - Raw data in Azure Data Lake (data lake pattern)
   - All formats: Parquet for structured, JSON for events

3. **Transformation:**
   - Azure Databricks or Fabric
   - Clean and validate data
   - Create conformed dimensions (products, stores, customers)
   - Aggregate into fact tables

4. **Serving:**
   - Load curated data to Synapse or Fabric
   - Create star schema model
   - Enable fast analytical queries

5. **Visualization:**
   - Power BI reports for:
     - Daily sales by region
     - Conversion rate from clickstream
     - Stock alerts for low inventory
   - Executive dashboard combining all three

---

## Mini Hands-On Flow

### Step 1: Ingest Sample Data to Lake
1. Create Azure Data Lake Storage (or use existing)
2. Create containers: raw, processed, curated
3. Upload sample CSV (sales data) and JSON (click events)

### Step 2: Build Cleaned "Sales" Table
1. Use Databricks or Fabric notebook
2. Read raw CSV
3. Clean: handle nulls, standardize dates
4. Write cleaned Parquet to processed folder

### Step 3: Create Star-Like Model
1. Create dimension tables: DimProduct, DimCustomer, DimDate
2. Create fact table: FactSales
3. Define relationships in Power BI or Synapse

### Step 4: Build Power BI Report
1. Connect to your model
2. Add Line Chart: Daily sales trend
3. Add Bar Chart: Sales by product category
4. Add Table: Top 10 products by revenue
5. Add Card: Total revenue KPI
6. Add Slicer: Date range filter

### Step 5: Enhance Report
1. Apply consistent formatting
2. Add tooltips
3. Configure interactions between visuals
4. Publish to workspace

---

## Expected Learning Outcomes

After this hands-on exercise, you should understand:

- **Pipeline thinking:** How data flows from source to insight
- **Modeling best practices:** Star schema design
- **Visualization choices:** Matching visuals to insights
- **Batch vs streaming:** When each approach is appropriate

---

## Common Mistakes to Avoid

1. **Using streaming when batch is enough**
   - Streaming adds significant complexity
   - Use batch unless seconds-level latency required
   - Store streaming data for batch reprocessing too

2. **Skipping data modeling and jumping directly to visuals**
   - Good model makes reports faster and simpler
   - Invest time in relationships and measures
   - Star schema pays dividends

3. **Overloading dashboards with too many visual types**
   - Too many visuals = confusing reports
   - One page, one story
   - Use tooltips for detail, not more visuals

4. **Ignoring refresh schedules**
   - Reports are useless if data is stale
   - Configure appropriate refresh frequency
   - Monitor for failures

---

## Quick Self-Check Questions

1. **Can you explain ETL vs ELT with one real example?**
   - ETL: Extract sales data → Transform in Data Factory → Load to Synapse
   - ELT: Load raw sales to Synapse → Transform using Synapse SQL

2. **Can you identify when to use warehouse vs lakehouse?**
   - Warehouse: Standard BI, known schemas, strict governance
   - Lakehouse: Need both ML and BI, schema flexibility, ACID on files

3. **Can you explain measure vs calculated column?**
   - Measure: Calculated at query time (SUM of sales)
   - Column: Stored in model (profit = revenue - cost)
