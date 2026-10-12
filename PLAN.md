# Task 1 — Computational Thinking Plan

## Thabo's Corner Store — Sales Insights System

Before coding the Sales Insights System, I used computational thinking to break the project into manageable steps, identify patterns in the data, focus on relevant information, and plan the order of development.

### 1. Decompose the Problem

I divided the project into smaller tasks:

1. Inspect and clean the raw `products.csv` and `sales.csv` files.
2. Design and create a relational SQLite database with `products` and `sales` tables.
3. Insert the cleaned data into the database and use SQL queries to analyse sales.
4. Use Python functions to calculate sales totals, identify low-stock products and analyse monthly trends.
5. Create charts using Matplotlib to present the results visually.
6. Implement password-hashing security and document the project.
7. Test the system and prepare the project for submission using Git and GitHub.

### 2. Pattern Recognition

I expected to find repeated data-quality problems in the CSV files, including:

- Missing product names and unit prices.
- Inconsistent capitalisation of product categories.
- Duplicate records.
- Different date formats in the sales data.
- Missing sale dates, quantities and payment methods.
- Sales that reference product IDs that do not exist in the products table.

Identifying these patterns helped me plan reusable cleaning steps instead of fixing each problem individually.

### 3. Abstraction

I focused on the information needed to answer Thabo's business questions. The important data includes product IDs, product names, categories, unit prices, quantities sold, sale dates, payment methods and customer types.

I planned to use reusable Python functions for data cleaning, database creation, SQL queries, sales analysis and chart generation. This keeps the program organised and avoids repeating code.

### 4. Algorithm and Order of Work

I planned to complete the modules in the following order:

1. `data_cleaning.py` — load and clean the raw CSV files.
2. `database.py` — create the SQLite tables, insert cleaned data and run SQL queries.
3. `analysis.py` — calculate sales statistics and identify business trends.
4. `visualize.py` — create charts from the analysis results.
5. `security.py` — implement password hashing and the login gate.
6. `main.py` — connect the modules and run the system.

I planned to test each module before relying on it in the complete program. This approach makes errors easier to identify and fix.

### Conclusion

Computational thinking helped me organise the project before coding. Decomposition divided the problem into smaller tasks, pattern recognition identified expected data-quality issues, abstraction focused attention on relevant information, and algorithm design established a logical development order.
