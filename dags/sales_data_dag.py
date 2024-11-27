from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

# Define the Python functions to run
def create_db():
    subprocess.run(["python", "scripts/create_db.py"])

def load_data():
    subprocess.run(["python", "scripts/load_data.py"])

def run_data_pipeline():
    subprocess.run(["python", "scripts/data_pipeline.py"])

# Define the default_args dictionary for Airflow
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 1),
    'retries': 1,
}

# Initialize the DAG
dag = DAG(
    'sales_data_pipeline',
    default_args=default_args,
    description='A simple sales data pipeline',
    schedule_interval=None,  
)

# Define tasks
task_create_db = PythonOperator(
    task_id='create_db',
    python_callable=create_db,
    dag=dag,
)

task_load_data = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

task_run_data_pipeline = PythonOperator(
    task_id='run_data_pipeline',
    python_callable=run_data_pipeline,
    dag=dag,
)

# Set task dependencies
task_create_db >> task_load_data >> task_run_data_pipeline
