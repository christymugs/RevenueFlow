import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Query 1: Total sales by product
cursor.execute('''
SELECT product_id, SUM(price * quantity) AS total_sales
FROM sales_data
GROUP BY product_id
''')
product_sales = cursor.fetchall()

print("Total Sales by Product:")
for row in product_sales:
    print(f"Product ID: {row[0]}, Total Sales: {row[1]}")

# Query 2: Total sales by customer
cursor.execute('''
SELECT customer_id, SUM(price * quantity) AS total_sales
FROM sales_data
GROUP BY customer_id
''')
customer_sales = cursor.fetchall()

print("\nTotal Sales by Customer:")
for row in customer_sales:
    print(f"Customer ID: {row[0]}, Total Sales: {row[1]}")

# Close the connection
conn.close()
