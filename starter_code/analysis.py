"""
analysis.py
------------
Task 4: Programming logic — functions, loops, conditionals and arrays.
"""


def total_sales_records(sales_rows: list) -> int:
    """Count sales records using a loop."""
    count = 0

    for row in sales_rows:
        count += 1

    return count


def low_stock_alert(products_rows: list, threshold: int = 5) -> list:
    """Return product names that need re-ordering."""
    alerts = []

    for product in products_rows:
        in_stock = product.get("in_stock")
        stock_count = product.get("stock_count")

        # If a stock count is available, flag low stock.
        if stock_count is not None:
            if stock_count <= threshold:
                alerts.append(product["product_name"])

        # Otherwise, use the in_stock field.
        elif in_stock is False or str(in_stock).strip().lower() == "false":
            alerts.append(product["product_name"])

    return alerts


def monthly_sales_trend(sales_rows: list) -> dict:
    """Calculate total quantity sold per month."""
    trend = {}

    for row in sales_rows:
        month = row["sale_date"][:7]
        quantity = row["quantity"]

        if month in trend:
            trend[month] += quantity
        else:
            trend[month] = quantity

    return trend


def classify_transaction_size(quantity: int) -> str:
    """Classify a transaction by its quantity."""
    if quantity >= 5:
        return "Bulk"
    elif quantity >= 2:
        return "Multiple"
    elif quantity == 1:
        return "Single"
    else:
        return "Invalid"


def average_basket_size(sales_rows: list) -> float:
    """Calculate the average quantity per sale."""
    total = 0
    count = 0

    for row in sales_rows:
        total += row["quantity"]
        count += 1

    if count == 0:
        return 0.0

    return round(total / count, 2)
