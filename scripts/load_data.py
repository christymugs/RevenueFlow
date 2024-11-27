import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Load data from CSV into the database
with open('../data/sales_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        cursor.execute('''
        INSERT INTO sales_data (order_id, customer_id, product_id, quantity, price, order_date)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (row[0], row[1], row[2], row[3], row[4], row[5]))

# Commit changes and close the connection
conn.commit()
conn.close()
print("Data loaded successfully.")
