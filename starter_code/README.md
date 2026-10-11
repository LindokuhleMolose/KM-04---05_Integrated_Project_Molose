# Thabo's Corner Store — Sales Insights System (Starter Code)

This is your starting scaffold. It already contains the **shape** of the
project — file structure, function signatures, imports and docstrings —
so you can focus on the actual data, database and programming logic
described in the Project Brief.

## Folder structure

```
starter_code/
├── README.md              <- this file
├── requirements.txt        <- Python packages you need
├── main.py                 <- entry point; runs your whole pipeline
├── data_cleaning.py         <- Task 2: load & clean the raw CSVs
├── database.py              <- Task 3: build the SQLite database + SQL queries
├── analysis.py               <- Task 4: functions/loops/conditionals for insights
├── visualize.py               <- Task 5: charts with matplotlib
└── security.py                 <- Task 6: simple login / password hashing
```

## Before you start

1. Make sure Python 3.10+ is installed: `python3 --version`
2. Create a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy the `data/` folder (provided separately) so it sits **next to**
   `starter_code/`, like this:
   ```
   project/
   ├── data/
   │   ├── products.csv
   │   └── sales.csv
   └── starter_code/
       └── ... (these files)
   ```

## Running your program

Once you've completed the TODOs in each file:

```bash
python main.py
```

## A note on the TODOs

Every function you need to complete has:
- A docstring explaining **what** it must do
- A `# TODO:` comment explaining **the specific steps**
- `raise NotImplementedError` as a placeholder — delete this once you've
  written your own code

Do not change the function names or the arguments they accept —
`main.py` calls them by name, and your facilitator's marking checklist
also references these exact names.

Good luck — and remember to commit your progress to GitHub regularly
as you complete each task, not just once at the end!


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
