# Airflow Practice Exercises

Practice your Airflow skills with these exercises.

---

## Setup

```python
# Basic DAG setup template
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "your_name",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "execution_timeout": timedelta(minutes=30)
}

with DAG(
    dag_id="practice_dag",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["practice"]
):
    # Your tasks here
    pass
```

---

## Exercise Set 1: DAG Basics

### Exercise 1.1: Create Your First DAG
Create a simple DAG with 3 tasks: extract, transform, load using BashOperator.

```python
# YOUR CODE HERE:



```

### Exercise 1.2: Set DAG Dependencies
Using the bit shift operator (>>), set the order: extract >> transform >> load

```python
# YOUR CODE HERE:



```

### Exercise 1.3: Add Default Arguments
Add default_args with 2 retries, 5 minute retry delay, and owner "dataeng".

```python
# YOUR CODE HERE:



```

### Exercise 1.4: Configure Scheduling
Create a DAG that runs at 2 AM daily starting from Jan 1, 2025.

```python
# YOUR CODE HERE:



```

---

## Exercise Set 2: Operators

### Exercise 2.1: PythonOperator
Create a task that prints "Hello from Airflow!"

```python
# YOUR CODE HERE:



```

### Exercise 2.2: BashOperator
Create a task that runs a shell command to print current date.

```python
# YOUR CODE HERE:



```

### Exercise 2.3: Multiple Tasks
Create 3 PythonOperator tasks that:
- Task 1: Returns the number 10
- Task 2: Multiplies the input by 2
- Task 3: Prints the final result

```python
# YOUR CODE HERE:



```

---

## Exercise Set 3: XCom

### Exercise 3.1: Push XCom
Push a value from one task using xcom_push.

```python
def push_value(**context):
    # Push "important_data" with value 100
    # YOUR CODE HERE:
    pass
```

### Exercise 3.2: Pull XCom
Pull the value pushed in previous exercise.

```python
def pull_value(**context):
    # Pull the value from push_value task
    # YOUR CODE HERE:
    pass
```

### Exercise 3.3: TaskFlow XCom
Use TaskFlow API to pass data between tasks automatically.

```python
from airflow.decorators import dag, task

@task
def extract():
    # Return a dictionary with name and age
    # YOUR CODE HERE:
    pass

@task
def transform(data):
    # Add 1 to age and return
    # YOUR CODE HERE:
    pass

@task
def load(data):
    # Print the final data
    # YOUR CODE HERE:
    pass

# Set up the flow
# YOUR CODE HERE:
```

---

## Exercise Set 4: Variables & Connections

### Exercise 4.1: Get Variable
Get a variable named "environment" with default "dev".

```python
# YOUR CODE HERE:



```

### Exercise 4.2: Set Variable
Set a variable "max_records" to 1000.

```python
# YOUR CODE HERE:



```

### Exercise 4.3: Use Connection
Use PostgresHook to connect to a database and run a query.

```python
# YOUR CODE HERE:



```

---

## Exercise Set 5: Sensors

### Exercise 5.1: FileSensor
Create a FileSensor that waits for a file at /tmp/data.csv

```python
# YOUR CODE HERE:



```

### Exercise 5.2: SqlSensor
Create a SqlSensor that checks if a table has rows.

```python
# YOUR CODE HERE:



```

### Exercise 5.3: Poke vs Reschedule
Explain when to use poke vs reschedule mode, then implement a sensor using reschedule.

```python
# YOUR CODE HERE:



```

---

## Exercise Set 6: TaskFlow API

### Exercise 6.1: Decorator-based DAG
Create a DAG using @dag and @task decorators.

```python
# YOUR CODE HERE:



```

### Exercise 6.2: Multiple Tasks with Dependencies
Create 4 tasks: start >> process1 >> process2 >> end

```python
# YOUR CODE HERE:



```

### Exercise 6.3: Conditional Branching
Create a BranchPythonOperator that chooses between two paths.

```python
# YOUR CODE HERE:



```

---

## Exercise Set 7: Trigger Rules

### Exercise 7.1: All Success (Default)
Create tasks where task3 runs only if task1 and task2 succeed.

```python
# YOUR CODE HERE:



```

### Exercise 7.2: One Failed
Create a task that runs if any upstream task fails.

```python
# YOUR CODE HERE:



```

### Exercise 7.3: All Done
Create a cleanup task that runs after all upstream tasks finish (regardless of success/failure).

```python
# YOUR CODE HERE:



```

---

## Exercise Set 8: Retry & Error Handling

### Exercise 8.1: Configure Retries
Add retry configuration to handle transient failures.

```python
# YOUR CODE HERE:



```

### Exercise 8.2: Custom Retry Logic
Create a task that checks a condition and raises an exception to trigger retry.

```python
# YOUR CODE HERE:



```

### Exercise 8.3: Timeout
Set execution_timeout for a long-running task.

```python
# YOUR CODE HERE:



```

---

## Exercise Set 9: Concurrency & Pools

### Exercise 9.1: Create Pool
Create a pool named "db_pool" with 5 slots.

```python
# YOUR CODE HERE:



```

### Exercise 9.2: Assign Pool to Task
Assign a task to use the db_pool.

```python
# YOUR CODE HERE:



```

### Exercise 9.3: Set DAG Concurrency
Limit a DAG to run maximum 2 tasks at a time.

```python
# YOUR CODE HERE:



```

---

## Exercise Set 10: Best Practices

### Exercise 10.1: Idempotent Task
Create a task that uses MERGE/UPSERT logic for idempotency.

```python
# YOUR CODE HERE:



```

### Exercise 10.2: Partition-Based Processing
Create a task that processes data for a specific partition (e.g., dt='2025-01-01').

```python
# YOUR CODE HERE:



```

### Exercise 10.3: Data Quality Check
Create a task that validates row count before proceeding.

```python
# YOUR CODE HERE:



```

---

## Challenge Exercises

### Challenge 1: ETL Pipeline
Build a complete ETL DAG:
1. Extract: Read from a mock source
2. Transform: Apply business logic
3. Load: Write to destination
4. Add retry and alerting

```python
# YOUR CODE HERE:



```

### Challenge 2: Dependent DAGs
Create two DAGs where DAG_B waits for DAG_A to complete using ExternalTaskSensor.

```python
# YOUR CODE HERE:



```

### Challenge 3: Dynamic Task Generation
Create a DAG that dynamically generates tasks based on a list of tables.

```python
# YOUR CODE HERE:



```

---

## Testing Your Code

Run these commands to test your DAGs:

```bash
# List all DAGs
airflow dags list

# Test DAG syntax
python -m py_compile your_dag.py

# Trigger a DAG manually
airflow dags trigger your_dag_id

# Run a specific task
airflow tasks test your_dag_id task_id execution_date
```

---

## Practice Complete!

After completing these exercises, you should be comfortable with:
- Creating and configuring DAGs
- Using different operators
- Working with XCom for task communication
- Handling variables and connections
- Using sensors for external dependencies
- Configuring retry and error handling
- Managing concurrency with pools
- Following Airflow best practices
