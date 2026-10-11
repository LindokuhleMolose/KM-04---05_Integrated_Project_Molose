import database

conn = database.get_connection("store.db")

queries = [
    ("1. Total revenue per product", database.query_total_revenue_per_product),
    ("2. Best-selling product", database.query_best_selling_product),
    ("3. Sales by payment method", database.query_sales_by_payment_method),
    ("4. Revenue by customer type", database.query_custom_one),
    ("5. Sales transactions per month", database.query_custom_two),
]

for title, query_function in queries:
    print(f"\n{title}")
    print("-" * len(title))
    for row in query_function(conn):
        print(row)

conn.close()