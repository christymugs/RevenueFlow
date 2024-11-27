# RevenueFlow

## Project Overview

This project focuses on building a **Sales Data Pipeline** using **SQL** and **Apache Airflow**. It involves collecting, transforming, and analyzing e-commerce sales data to provide valuable insights into sales performance over time. The pipeline uses **Python**, **SQL**, **SQLite**, and **Apache Airflow** for orchestration, and the data is stored in an SQLite database.

### Technologies Used:
- **Python 3**
- **SQLite** for the database
- **Apache Airflow** for workflow orchestration
- **SQL** for data transformation and queries

## Project Setup

### Prerequisites
To run this project, you need to have the following tools installed on your machine:
- Python 3.x
- Apache Airflow
- SQLite
- pip (Python package manager)

### Installation

#### Step 1: Clone the Repository

Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/sales-data-pipeline.git
cd sales-data-pipeline
```

#### Step 2: Install Required Packages

Create a virtual environment (optional but recommended) and install the dependencies:
```bash
python3 -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
```

#### Step 3: Set Up Apache Airflow

To install Apache Airflow, run the following command:
```bash
pip install apache-airflow
```
Set up Airflow's environment by initializing the database:
```bash
airflow db init
```
Start the Airflow web server and scheduler:
```bash
airflow webserver --port 8080  
airflow scheduler            
```
## Project Structure
```bash
sales-data-pipeline/
│
├── data/
│   └── sales_data.csv        # Sample sales data in CSV format
│
├── scripts/
│   ├── create_db.py          # Script to create SQLite database from CSV
│   ├── load_data.py          # Script to load data into SQLite
│   └── data_pipeline.py      # Main pipeline logic with SQL queries
│
├── dags/
│   └── sales_data_dag.py     # Apache Airflow DAG for orchestrating the data pipeline
│
├── requirements.txt          # Project dependencies
└── README.md                 # Project overview and setup instructions
```

## Database Creation
The project uses an SQLite database to store and manage sales data. To create the database and load the sample data, follow these steps:

1. Create the SQLite Database: Run the following command to create the database and import the data:
```bash
python scripts/create_db.py
```
2. Load Data into Database: The data is stored in the data/sales_data.csv file. To load this data into the SQLite database, run:
```bash
python scripts/load_data.py
```

## Data Pipeline
The main logic for processing the data is located in the scripts/data_pipeline.py. This script performs the following tasks:

1. Reads data from the SQLite database.
2. Transforms and analyzes the data using SQL queries.
3. Outputs meaningful insights, such as total sales, sales by product, and sales by customer.

### Example SQL Queries:
-- Total sales by product
SELECT product_id, SUM(price * quantity) AS total_sales
FROM sales_data
GROUP BY product_id;

-- Total sales by customer
SELECT customer_id, SUM(price * quantity) AS total_sales
FROM sales_data
GROUP BY customer_id;

## Results

Here's a preview of the sales data:
```bash

order_id	customer_id	product_id	quantity	price	order_date
1	        101	201	                 2	        25.50	2024-11-01
2	        102	202	                 1	        50.00	2024-11-01
3	        103	203	                 3	        15.00	2024-11-02
...	...	...	...	...	...
```

## Conclusion
This project demonstrates how to use SQL and Apache Airflow to build an automated data pipeline that processes and analyzes e-commerce sales data. The pipeline extracts data from a CSV file, stores it in an SQLite database, and performs meaningful transformations and analysis. The results can be used to generate business insights and optimize sales strategies.
