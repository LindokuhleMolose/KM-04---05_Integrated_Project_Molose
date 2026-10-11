# KM-04 + KM-05 Integrated Project Package

**Thabo's Corner Store — Sales Insights System**
Occupational Certificate: Artificial Intelligence Software Developer · NQF Level 4

This package contains everything needed to run the integrated project
covering KM-04 (Data & Databases) and KM-05 (Programming & Python).

## What's in this package

| File / Folder | Purpose |
|---|---|
| `Project_Brief_and_Instructions.docx` | The full project brief: scenario, tasks, resources, submission steps and marking rubric. **Give this to students first.** |
| `GitHub_and_VSCode_Setup_Guide.docx` | A step-by-step guide for students to create a GitHub account, install Git, connect VS Code, and push their project as evidence. |
| `data/products.csv` | Raw product data (14 products), with deliberate data-quality issues for students to clean. |
| `data/sales.csv` | Raw sales transaction data (71 records), with deliberate data-quality issues for students to clean. |
| `starter_code/` | A Python project scaffold (five modules + main.py) with docstrings and TODO comments, but no solved logic — this is the students' starting point, not a solution. |

## Distributing this to students

1. Share this whole folder (or the zip it came in) with students — for
   example as a single download on UpSkill, or in a shared class folder.
2. Students should keep `data/` and `starter_code/` side by side in
   their own project folder (see `starter_code/README.md` for the exact
   layout they need).
3. Direct students to read `Project_Brief_and_Instructions.docx` first,
   then `GitHub_and_VSCode_Setup_Guide.docx` before they begin coding.

## For facilitators: suggested pacing

This project is designed to be completed across roughly 2–3 weeks of
part-time study, alongside the KM-04 and KM-05 contact sessions:

- **Week 1:** Task 1 (planning) and Task 2 (data cleaning) — pairs well
  with revisiting KM-04 Sections 1–2.
- **Week 2:** Tasks 3–5 (database, SQL, programming logic, charts) —
  pairs well with KM-04 Sections 4–7 and KM-05 Section 3.
- **Week 3:** Tasks 6–8 (security, documentation, GitHub submission) —
  pairs well with KM-04 Section 8 and KM-05 Section 4.

A reference solution is available from your internal moderation
process — it is intentionally not included in this student-facing
package.


# LINDOKUHLE'S PART
# Thabo's Corner Store — Sales Insights System

## Project Overview

This project develops a Sales Insights System for Thabo's Corner Store. The system uses Python, pandas, SQLite and Matplotlib to clean sales data, store information in a database, analyse sales performance and present findings that can help with business decisions.

## Task 1: Computational Thinking Plan

Before developing the system, I used the four computational thinking pillars to plan my work.

- **Decomposition:** I divided the project into data cleaning, database creation, sales analysis, visualisation, security and documentation.
- **Pattern Recognition:** I identified possible data-quality problems such as duplicate records, missing values, inconsistent categories, different date formats and invalid product IDs.
- **Abstraction:** I focused on the information needed for sales analysis, including product IDs, product names, prices, quantities, sale dates and payment methods.
- **Algorithm Design:** I planned to clean the data first, create and populate the database, run SQL queries, analyse the results and create charts.

The full planning document is saved separately as `PLAN.md` in the main project folder.

## Task 2: Data Cleaning

### Objective

The objective of Task 2 was to load the raw product and sales CSV files, identify data-quality problems and prepare clean data for storage in the SQLite database.

### Tools Used

- Python
- pandas
- CSV files

### Cleaning Process

I implemented the data-cleaning functions in `starter_code/data_cleaning.py`.

The cleaning process includes:

1. Loading `products.csv` and `sales.csv` using pandas.
2. Removing duplicate rows.
3. Removing product records with missing product names or unit prices.
4. Standardising product category capitalisation and removing surrounding spaces.
5. Removing sales records with missing quantities.
6. Filling missing payment methods with `Unknown`.
7. Converting sale dates into a consistent `YYYY-MM-DD` format.
8. Removing sales with missing or invalid dates.
9. Removing sales records whose product IDs do not match valid product IDs.
10. Producing a summary showing the number of raw and cleaned rows.

### Cleaning Results

The program produced the following summary:

| Dataset | Raw rows | Clean rows | Rows removed |
|---|---:|---:|---:|
| Products | 16 | 12 | 4 |
| Sales | 71 | 43 | 28 |

These results show that the cleaning process removed records that did not meet the selected data-quality rules.

### Conclusion

Task 2 prepared the data for database storage and analysis. Cleaning the data helps reduce errors and makes the results more reliable. Missing payment methods were retained as `Unknown`, while sales with missing or invalid dates, missing quantities or invalid product IDs were removed.

## Task 3: Database Design and SQL Queries

### Objective

The objective of Task 3 was to create a relational SQLite database, store the cleaned product and sales data, and use SQL queries to answer business questions.

### Database Design

I implemented the database functions in `starter_code/database.py`.

The database contains two tables:

**Products table**
- `product_id` — primary key
- `product_name`
- `category`
- `unit_price`

**Sales table**
- `sale_id` — primary key
- `product_id` — foreign key referencing the products table
- `quantity`
- `sale_date`
- `payment_method`
- `customer_type`

The relationship between the tables allows sales records to be linked to the products sold.

### SQL Queries and Results

I tested five queries using `test_database.py`.

**1. Total revenue per product**

The query calculates revenue by multiplying the quantity sold by the product's unit price.

The highest-revenue product in the results was **5kg Maize Meal**, with total revenue of **801.00**.

**2. Best-selling product**

The query calculates the total quantity sold for each product.

**Bar One Chocolate** was the best-selling product by quantity, with 16 units sold.

**3. Sales by payment method**

The query counts the number of sales transactions for each payment method.

| Payment method | Number of sales |
|---|---:|
| Cash | 14 |
| Mobile Money | 11 |
| Card | 10 |
| Unknown | 8 |

Cash was the most frequently recorded payment method.

**4. Revenue by customer type**

The query calculates total revenue for each customer type.

| Customer type | Total revenue |
|---|---:|
| Regular | 861.50 |
| Walk-in | 832.00 |
| Missing value | 796.00 |

Regular customers generated the highest recorded revenue among the named customer types. The results also contain sales with missing customer-type information.

**5. Sales transactions per month**

The query counts the number of transactions in each month based on the cleaned sale dates. The results covered dates from January to December 2026, with transactions recorded in several months.

### Conclusion

Task 3 successfully created the database and returned results for all five SQL queries. The results identify products generating revenue, the product with the highest quantity sold, payment-method patterns and revenue by customer type. Missing customer-type values should be reviewed when improving the system.

## Technologies Used

- Python
- pandas
- SQLite
- Matplotlib
- Visual Studio Code
- Git and GitHub

## Project Files

- `PLAN.md` — computational thinking plan.
- `data/products.csv` — raw product data.
- `data/sales.csv` — raw sales data.
- `starter_code/data_cleaning.py` — data-cleaning functions.
- `starter_code/database.py` — database and SQL query functions.
- `starter_code/analysis.py` — sales analysis functions.
- `starter_code/visualize.py` — chart generation functions.
- `starter_code/security.py` — security functions.
- `starter_code/main.py` — main program.
- `README.md` — project documentation.

## Running the Project

Open the project in Visual Studio Code, open the terminal and navigate to the `starter_code` folder. Run:

```powershell
python main.py
```

The program may require the remaining analysis, visualisation and security tasks to be completed before the full system runs from beginning to end.



