# Power BI Practice Exercises

Practice your Power BI skills with these exercises.

---

## Setup - Sample Data

```
Sales Data Sample:
| OrderID | Date       | Product | Category   | Customer | Region | Quantity | Sales | Cost |
|---------|------------|---------|------------|----------|--------|----------|-------|------|
| 1       | 2024-01-05 | Laptop  | Electronics| John     | East   | 2        | 2000  | 1400 |
| 2       | 2024-01-10 | Mouse   | Electronics| Jane     | West   | 10       | 300   | 180  |
| 3       | 2024-01-15 | Chair   | Furniture  | Bob      | East   | 1        | 400   | 250  |
| 4       | 2024-02-01 | Laptop  | Electronics| John     | East   | 1        | 1000  | 700  |
| 5       | 2024-02-10 | Desk    | Furniture  | Alice    | West   | 2        | 600   | 400  |

Customer Data:
| CustomerID | Name  | Email             | City     | State | Country |
|------------|-------|-------------------|----------|-------|---------|
| 1          | John  | john@email.com    | New York | NY    | USA     |
| 2          | Jane  | jane@email.com    | Los Angeles| CA  | USA     |
| 3          | Bob   | bob@email.com     | Chicago  | IL    | USA     |
| 4          | Alice | alice@email.com   | Seattle  | WA    | USA     |

Product Data:
| ProductID | Product | Category   | Brand   | Price |
|-----------|---------|------------|---------|-------|
| 1         | Laptop  | Electronics| Dell    | 1000  |
| 2         | Mouse   | Electronics| Logitech| 30    |
| 3         | Chair   | Furniture  | HermanMiller| 400 |
| 4         | Desk    | Furniture  | IKEA    | 300   |
```

---

## Exercise Set 1: Power Query Basics

### Exercise 1.1: Connect to Data Source
Connect to the sample sales data (CSV/Excel) using Power Query.

```m
// YOUR CODE HERE:
// Use Get Data to connect to file
// Navigate to folder and select file
```

### Exercise 1.2: Remove Columns
Remove unnecessary columns from the sales data.

```m
// YOUR CODE HERE:
// Remove columns: OrderID, Customer (keep CustomerID)
```

### Exercise 1.3: Filter Rows
Filter to show only orders with Sales > 500.

```m
// YOUR CODE HERE:
// Use Table.SelectRows
```

### Exercise 1.4: Rename Columns
Rename columns to more descriptive names.

```m
// YOUR CODE HERE:
// Rename: Sales -> SalesAmount, Cost -> CostAmount
```

### Exercise 1.5: Change Data Types
Ensure correct data types for all columns.

```m
// YOUR CODE HERE:
// Date -> Date, Quantity -> Whole Number, Sales -> Decimal
```

### Exercise 1.6: Remove Duplicates
Remove duplicate rows based on CustomerID.

```m
// YOUR CODE HERE:
// Use Table.Distinct
```

### Exercise 1.7: Split Column
Split the Customer column into FirstName and LastName.

```m
// YOUR CODE HERE:
// Split by space delimiter
```

### Exercise 1.8: Merge Columns
Merge FirstName and LastName into FullName.

```m
// YOUR CODE HERE:
// Use Text.Combine or custom column
```

---

## Exercise Set 2: Power Query Advanced

### Exercise 2.1: Conditional Column
Create a new column based on conditions.

```m
// YOUR CODE HERE:
// If Sales > 1000 -> "High", > 500 -> "Medium", else "Low"
```

### Exercise 2.2: Group By and Aggregate
Group by Category and calculate total sales.

```m
// YOUR CODE HERE:
// Use Table.Group
```

### Exercise 2.3: Pivot Column
Pivot the Category column to create columns for each category.

```m
// YOUR CODE HERE:
// Use Table.Pivot
```

### Exercise 2.4: Unpivot Columns
Unpivot category columns back to rows.

```m
// YOUR CODE HERE:
// Use Table.UnpivotOtherColumns
```

### Exercise 2.5: Merge Queries
Join Sales with Customer data.

```m
// YOUR CODE HERE:
// Use Table.NestedJoin and expand
```

### Exercise 2.6: Append Queries
Combine two tables vertically.

```m
// YOUR CODE HERE:
// Use Table.Combine
```

### Exercise 2.7: Create Custom Function
Create a function to clean text (trim, proper case).

```m
// YOUR CODE HERE:
// Create custom function for text cleaning
```

### Exercise 2.8: Fill Down
Fill down null values in a column.

```m
// YOUR CODE HERE:
// Use Table.FillDown
```

---

## Exercise Set 3: Data Modeling

### Exercise 3.1: Create Star Schema
Design a star schema with FactSales and dimension tables.

```
// YOUR CODE HERE:
// Fact: FactSales (SalesKey, DateKey, ProductKey, CustomerKey, Quantity, SalesAmount)
// Dim: DimDate, DimProduct, DimCustomer
```

### Exercise 3.2: Create Relationships
Create relationships between fact and dimension tables.

```
// YOUR CODE HERE:
// FactSales[DateKey] -> DimDate[DateKey]
// FactSales[ProductKey] -> DimProduct[ProductKey]
// FactSales[CustomerKey] -> DimCustomer[CustomerKey]
```

### Exercise 3.3: Configure Relationship Cardinality
Set appropriate cardinality for relationships.

```
// YOUR CODE HERE:
// One to Many (Dim -> Fact)
```

### Exercise 3.4: Create Date Hierarchy
Create a date hierarchy in DimDate.

```
// YOUR CODE HERE:
// Year -> Quarter -> Month -> Day
```

### Exercise 3.5: Create Calculated Column
Add FullName column to DimCustomer.

```dax
// YOUR CODE HERE:
Full Name = DimCustomer[FirstName] & " " & DimCustomer[LastName]
```

### Exercise 3.6: Mark as Date Table
Mark DimDate as the date table.

```
// YOUR CODE HERE:
// Use Mark as Date Table in Modeling tab
```

### Exercise 3.7: Role-Playing Dimension
Handle multiple date fields (OrderDate, ShipDate).

```dax
// YOUR CODE HERE:
// Use USERELATIONSHIP for inactive relationships
```

---

## Exercise Set 4: DAX Basic Measures

### Exercise 4.1: Sum Measure
Create Total Sales measure.

```dax
// YOUR CODE HERE:
Total Sales := SUM(FactSales[SalesAmount])
```

### Exercise 4.2: Count Measure
Create Order Count measure.

```dax
// YOUR CODE HERE:
Order Count := COUNT(FactSales[SalesKey])
```

### Exercise 4.3: Average Measure
Create Average Order Value measure.

```dax
// YOUR CODE HERE:
Avg Order Value := AVERAGE(FactSales[SalesAmount])
```

### Exercise 4.4: Min/Max Measures
Create measures for min and max order values.

```dax
// YOUR CODE HERE:
Min Order := MIN(FactSales[SalesAmount])
Max Order := MAX(FactSales[SalesAmount])
```

### Exercise 4.5: Distinct Count
Create measure for unique customers.

```dax
// YOUR CODE HERE:
Unique Customers := DISTINCTCOUNT(FactSales[CustomerKey])
```

### Exercise 4.6: Calculate with Filter
Create measure for Electronics sales only.

```dax
// YOUR CODE HERE:
Electronics Sales := CALCULATE(SUM(FactSales[SalesAmount]), DimProduct[Category] = "Electronics")
```

### Exercise 4.7: Iterator Function
Create Total Profit using SUMX.

```dax
// YOUR CODE HERE:
Total Profit := SUMX(FactSales, FactSales[SalesAmount] - FactSales[CostAmount])
```

### Exercise 4.8: Count Rows
Count total number of orders.

```dax
// YOUR CODE HERE:
Total Orders := COUNTROWS(FactSales)
```

---

## Exercise Set 5: DAX Filter Context

### Exercise 5.1: ALL Function
Create measure ignoring all filters.

```dax
// YOUR CODE HERE:
Sales All := CALCULATE(SUM(FactSales[SalesAmount]), ALL(DimProduct))
```

### Exercise 5.2: ALLEXCEPT
Remove filters except Year.

```dax
// YOUR CODE HERE:
Sales All Years Except Month := CALCULATE(SUM(FactSales[SalesAmount]), ALLEXCEPT(DimDate, DimDate[Year]))
```

### Exercise 5.3: ALLSELECTED
Get sales for selected values.

```dax
// YOUR CODE HERE:
Sales Selected := CALCULATE(SUM(FactSales[SalesAmount]), ALLSELECTED())
```

### Exercise 5.4: CALCULATE with Multiple Filters
Sales for 2024 Electronics.

```dax
// YOUR CODE HERE:
Sales 2024 Electronics := CALCULATE(SUM(FactSales[SalesAmount]), DimDate[Year] = 2024, DimProduct[Category] = "Electronics")
```

### Exercise 5.5: Variable Example
Use variables to simplify complex calculation.

```dax
// YOUR CODE HERE:
Profit Margin := VAR Sales = SUM(FactSales[SalesAmount]) VAR Cost = SUM(FactSales[CostAmount]) RETURN DIVIDE(Sales - Cost, Sales)
```

---

## Exercise Set 6: Time Intelligence

### Exercise 6.1: Total YTD
Calculate year-to-date sales.

```dax
// YOUR CODE HERE:
Sales YTD := TOTALYTD(SUM(FactSales[SalesAmount]), DimDate[Date])
```

### Exercise 6.2: Total MTD
Calculate month-to-date sales.

```dax
// YOUR CODE HERE:
Sales MTD := TOTALMTD(SUM(FactSales[SalesAmount]), DimDate[Date])
```

### Exercise 6.3: Total QTD
Calculate quarter-to-date sales.

```dax
// YOUR CODE HERE:
Sales QTD := TOTALQTD(SUM(FactSales[SalesAmount]), DimDate[Date])
```

### Exercise 6.4: Same Period Last Year
Compare with previous year.

```dax
// YOUR CODE HERE:
Sales PY := CALCULATE(SUM(FactSales[SalesAmount]), SAMEPERIODLASTYEAR(DimDate[Date]))
```

### Exercise 6.5: Year Over Year Growth
Calculate YoY percentage growth.

```dax
// YOUR CODE HERE:
YoY Growth := VAR Current = SUM(FactSales[SalesAmount]) VAR Previous = CALCULATE(SUM(FactSales[SalesAmount]), SAMEPERIODLASTYEAR(DimDate[Date])) RETURN DIVIDE(Current - Previous, Previous)
```

### Exercise 6.6: Moving Average
Calculate 3-month moving average.

```dax
// YOUR CODE HERE:
Moving Avg 3M := AVERAGEX(DATESINPERIOD(DimDate[Date], LASTDATE(DimDate[Date]), -3, MONTH), CALCULATE(SUM(FactSales[SalesAmount])))
```

### Exercise 6.7: Running Total
Calculate running total for the year.

```dax
// YOUR CODE HERE:
Running Total := CALCULATE(SUM(FactSales[SalesAmount]), FILTER(ALL(DimDate), DimDate[Date] <= MAX(DimDate[Date])))
```

---

## Exercise Set 7: Advanced DAX

### Exercise 7.1: RANKX
Rank customers by sales.

```dax
// YOUR CODE HERE:
Customer Rank := RANKX(ALL(DimCustomer), CALCULATE(SUM(FactSales[SalesAmount])))
```

### Exercise 7.2: Top N Filter
Show top 10 products.

```dax
// YOUR CODE HERE:
Top 10 Products := TOPN(10, ALL(DimProduct), CALCULATE(SUM(FactSales[SalesAmount])), DESC)
```

### Exercise 7.3: ABC Analysis
Categorize products by sales contribution.

```dax
// YOUR CODE HERE:
Product Category := VAR SalesSum = SUM(FactSales[SalesAmount]) VAR Total = CALCULATE(SUM(FactSales[SalesAmount]), ALL(DimProduct)) VAR Pct = DIVIDE(SalesSum, Total) RETURN IF(Pct > 0.7, "C", IF(Pct > 0.4, "B", "A"))
```

### Exercise 7.4: RELATED Function
Get product price in fact table.

```dax
// YOUR CODE HERE:
Product Price := RELATED(DimProduct[Price])
```

### Exercise 7.5: RELATEDTABLE
Count orders per customer.

```dax
// YOUR CODE HERE:
Order Count := COUNTROWS(RELATEDTABLE(FactSales))
```

### Exercise 7.6: HASONEVALUE
Check single selection in slicer.

```dax
// YOUR CODE HERE:
Selected Category Sales := IF(HASONEVALUE(DimProduct[Category]), CALCULATE(SUM(FactSales[SalesAmount])), "Multiple Categories Selected")
```

### Exercise 7.7: SWITCH Function
Use SWITCH for conditional logic.

```dax
// YOUR CODE HERE:
Quarter Label := SWITCH(DimDate[Quarter], 1, "Q1", 2, "Q2", 3, "Q3", 4, "Q4", "Unknown")
```

---

## Exercise Set 8: Visualizations

### Exercise 8.1: Create Bar Chart
Create bar chart showing sales by category.

```
// YOUR CODE HERE:
// Visualizations: Bar Chart
// Axis: Category
// Values: Total Sales
```

### Exercise 8.2: Create Line Chart
Create line chart showing sales trend over time.

```
// YOUR CODE HERE:
// Visualizations: Line Chart
// Axis: Date (Month)
// Values: Total Sales
```

### Exercise 8.3: Create Pie Chart
Create pie chart showing sales by region.

```
// YOUR CODE HERE:
// Visualizations: Pie Chart
// Legend: Region
// Values: Total Sales
```

### Exercise 8.4: Create Table
Create table with multiple columns.

```
// YOUR CODE HERE:
// Columns: Product, Category, Total Sales, Order Count
```

### Exercise 8.5: Create Matrix
Create matrix showing sales by Category and Region.

```
// YOUR CODE HERE:
// Use Matrix visual with hierarchies
```

### Exercise 8.6: Create KPI Visual
Create KPI showing target vs actual.

```
// YOUR CODE HERE:
// Indicator: Total Sales
// Target: 10000
// Trend axis: Month
```

### Exercise 8.7: Create Map Visual
Create map showing sales by location.

```
// YOUR CODE HERE:
// Location: City or State
// Bubble size: Sales Amount
```

### Exercise 8.8: Create Slicer
Create slicer for category selection.

```
// YOUR CODE HERE:
// Use Category field in slicer
// Test single and multi-select
```

---

## Exercise Set 9: Reports & Dashboards

### Exercise 9.1: Design Report Page
Create a sales overview report page.

```
// YOUR CODE HERE:
// Add title, KPI cards, charts
// Arrange layout logically
```

### Exercise 9.2: Add Drill-Through
Create drill-through page for product details.

```
// YOUR CODE HERE:
// Create detail page
// Add Drill-through fields
// Test drill-through from main page
```

### Exercise 9.3: Add Bookmarks
Create bookmarks for different view states.

```
// YOUR CODE HERE:
// Save visual states
// Add bookmark buttons
```

### Exercise 9.4: Add Buttons and Navigation
Add page navigation buttons.

```
// YOUR CODE HERE:
// Create buttons
// Configure page navigation action
```

### Exercise 9.5: Add Tooltips
Configure custom tooltips.

```
// YOUR CODE HERE:
// Create tooltip page
// Configure visual tooltips
```

### Exercise 9.6: Sync Slicers
Sync slicers across pages.

```
// YOUR CODE HERE:
// Use Sync Slicers pane
```

---

## Exercise Set 10: Power BI Service

### Exercise 10.1: Publish Report
Publish report to Power BI Service.

```
// YOUR CODE HERE:
// File > Publish
// Select workspace
```

### Exercise 10.2: Create Workspace
Create a new workspace for collaboration.

```
// YOUR CODE HERE:
// In Power BI Service
// Configure workspace settings
```

### Exercise 10.3: Configure Scheduled Refresh
Set up automatic data refresh.

```
// YOUR CODE HERE:
// Dataset settings > Scheduled refresh
// Configure frequency
```

### Exercise 10.4: Share Report
Share report with colleagues.

```
// YOUR CODE HERE:
// Use Share button
// Configure permissions
```

### Exercise 10.5: Create Dashboard
Pin visuals to create dashboard.

```
// YOUR CODE HERE:
// Pin from report
// Arrange tiles
```

### Exercise 10.6: Row-Level Security
Configure RLS for regional access.

```dax
// YOUR CODE HERE:
// Create role: RegionalManager
// DAX: DimRegion[Region] = USERNAME()
```

---

## Exercise Set 11: Advanced Features

### Exercise 11.1: Incremental Refresh
Configure incremental refresh for large dataset.

```
// YOUR CODE HERE:
// Define RangeStart, RangeEnd parameters
// Configure refresh policy
```

### Exercise 11.2: Composite Model
Set storage mode for different tables.

```
// YOUR CODE HERE:
// Import for dimensions
// DirectQuery for large tables
```

### Exercise 11.3: Create Aggregation
Create aggregation for performance.

```
// YOUR CODE HERE:
// Configure aggregation table
```

---

## Challenge Exercises

### Challenge 1: Sales Dashboard
Create a complete sales dashboard with:
1. KPI cards (Total Sales, Orders, Avg Order)
2. Sales trend line chart
3. Top 10 products bar chart
4. Sales by region map
5. Category pie chart
6. Interactive slicers

```
// YOUR CODE HERE:



```

### Challenge 2: Financial Report
Create financial report with:
1. Revenue, Cost, Profit measures
2. Profit margin calculations
3. YoY comparison
4. Monthly/Quarterly/Yearly toggle

```
// YOUR CODE HERE:



```

### Challenge 3: Customer Analysis
Create customer analysis with:
1. Customer ranking
2. Customer segmentation (ABC)
3. Cohort analysis
4. Retention metrics

```
// YOUR CODE HERE:



```

---

## Testing Your DAX

### Quick Reference

```dax
// Test measures in DAX Studio or Power BI
EVALUATE
CALCULATETABLE(
    ADDCOLUMNS(
        VALUES(DimCustomer),
        "Total Sales",
        CALCULATE(SUM(FactSales[SalesAmount]))
    ),
    ORDER BY [Total Sales] DESC
)
```

---

## Practice Complete!

After completing these exercises, you should be comfortable with:
- Power Query transformations
- Data modeling and relationships
- Basic DAX measures
- Filter context and CALCULATE
- Time intelligence functions
- Advanced DAX patterns
- Creating visualizations
- Building reports and dashboards
- Power BI Service features
- Row-level security

---

## Next Steps

1. Practice with real datasets
2. Explore Power BI Community
3. Learn Power BI best practices
4. Build portfolio dashboards
5. Prepare for Power BI certifications
