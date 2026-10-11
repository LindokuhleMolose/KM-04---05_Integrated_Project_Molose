"""
database.py
------------
Task 3: Build a relational database from your cleaned data.

This module covers KM-04 topics: Introduction to Databases (DBMS,
components, characteristics) and Structured Query Language (SQL).

You will use Python's built-in sqlite3 module — no extra install
needed. SQLite stores the whole database in a single file, which makes
it perfect for a student project (and easy to include as evidence).

By the end of this file you must be able to:
  1. Create a database file (store.db) with two related tables.
  2. Insert your cleaned data into those tables.
  3. Run at least FIVE meaningful SQL queries against the data,
     including at least one JOIN and one aggregation (SUM, COUNT, AVG).
"""

import sqlite3


def get_connection(db_path: str = "store.db") -> sqlite3.Connection:
    """
    Open (and create, if needed) the SQLite database file.

    Returns:
        an open sqlite3.Connection
    """
    return sqlite3.connect(db_path)


def create_tables(conn: sqlite3.Connection) -> None:
    """
    Create the `products` and `sales` tables if they don't already exist.
    """

    # Products table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id TEXT PRIMARY KEY,
            product_name TEXT NOT NULL,
            category TEXT,
            unit_price REAL
        )
    """)

    # Sales table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            sale_id TEXT PRIMARY KEY,
            product_id TEXT,
            quantity INTEGER,
            sale_date TEXT,
            payment_method TEXT,
            customer_type TEXT,
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    """)

    conn.commit()


def insert_products(conn: sqlite3.Connection, products_df) -> None:
    """
    Insert every row of the cleaned products DataFrame into the
    products table.
    """

    sql = """
        INSERT INTO products
        (product_id, product_name, category, unit_price)
        VALUES (?, ?, ?, ?)
    """

    rows = [
        (
            row.product_id,
            row.product_name,
            row.category,
            row.unit_price
        )
        for row in products_df.itertuples(index=False)
    ]

    conn.executemany(sql, rows)
    conn.commit()


def insert_sales(conn: sqlite3.Connection, sales_df) -> None:
    """
    Insert every row of the cleaned sales DataFrame into the sales table.
    """

    sql = """
        INSERT INTO sales
        (sale_id, product_id, quantity, sale_date,
         payment_method, customer_type)
        VALUES (?, ?, ?, ?, ?, ?)
    """

    rows = [
        (
            row.sale_id,
            row.product_id,
            row.quantity,
            row.sale_date,
            row.payment_method,
            row.customer_type
        )
        for row in sales_df.itertuples(index=False)
    ]

    conn.executemany(sql, rows)
    conn.commit()


# ---------------------------------------------------------------------
# SQL QUERIES
# ---------------------------------------------------------------------

def query_total_revenue_per_product(conn: sqlite3.Connection):
    """
    Return each product's name and its total revenue
    (quantity * unit_price), highest revenue first.
    """

    sql = """
        SELECT
            p.product_name,
            SUM(s.quantity * p.unit_price) AS total_revenue
        FROM sales AS s
        JOIN products AS p
            ON s.product_id = p.product_id
        GROUP BY p.product_id, p.product_name
        ORDER BY total_revenue DESC
    """

    return conn.execute(sql).fetchall()


def query_best_selling_product(conn: sqlite3.Connection):
    """
    Return the single product with the highest total quantity sold.
    """

    sql = """
        SELECT
            p.product_name,
            SUM(s.quantity) AS total_quantity
        FROM sales AS s
        JOIN products AS p
            ON s.product_id = p.product_id
        GROUP BY p.product_id, p.product_name
        ORDER BY total_quantity DESC
        LIMIT 1
    """

    return conn.execute(sql).fetchall()


def query_sales_by_payment_method(conn: sqlite3.Connection):
    """
    Return the number of sales transactions per payment_method.
    """

    sql = """
        SELECT
            payment_method,
            COUNT(*) AS number_of_sales
        FROM sales
        GROUP BY payment_method
        ORDER BY number_of_sales DESC
    """

    return conn.execute(sql).fetchall()


def query_custom_one(conn: sqlite3.Connection):
    """
    Business question:
    Which customer type generates the most revenue?
    """

    sql = """
        SELECT
            s.customer_type,
            SUM(s.quantity * p.unit_price) AS total_revenue
        FROM sales AS s
        JOIN products AS p
            ON s.product_id = p.product_id
        GROUP BY s.customer_type
        ORDER BY total_revenue DESC
    """

    return conn.execute(sql).fetchall()


def query_custom_two(conn: sqlite3.Connection):
    """
    Business question:
    How many sales transactions happened in each month?
    """

    sql = """
        SELECT
            substr(sale_date, 1, 7) AS month,
            COUNT(*) AS number_of_sales
        FROM sales
        GROUP BY month
        ORDER BY month
    """

    return conn.execute(sql).fetchall()