# Basic Concepts Practice Exercises

Practice your data engineering basic skills with these exercises.

---

## Exercise Set 1: Git Version Control

### Exercise 1.1: Initialize Repository
Initialize a new Git repository.

```bash
# YOUR CODE HERE:
# Create folder and initialize git
```

### Exercise 1.2: Create and Commit Files
Create a file and commit to repository.

```bash
# YOUR CODE HERE:
# Add file, commit with message
```

### Exercise 1.3: View History
View git log with different formats.

```bash
# YOUR CODE HERE:
# View log, oneline, detailed
```

### Exercise 1.4: Create Branch
Create and switch to a new branch.

```bash
# YOUR CODE HERE:
# Create feature branch, switch to it
```

### Exercise 1.5: Merge Branch
Merge feature branch into main.

```bash
# YOUR CODE HERE:
# Switch to main, merge feature
```

### Exercise 1.6: Handle Merge Conflict
Simulate and resolve a merge conflict.

```bash
# YOUR CODE HERE:
# Create conflict, resolve, commit
```

### Exercise 1.7: Push to Remote
Add remote and push to GitHub.

```bash
# YOUR CODE HERE:
# Add origin, push code
```

### Exercise 1.8: Pull Changes
Pull latest changes from remote.

```bash
# YOUR CODE HERE:
# Pull and merge changes
```

---

## Exercise Set 2: Command Line & Linux

### Exercise 2.1: Navigate Filesystem
Navigate and list files.

```bash
# YOUR CODE HERE:
# List files, change directories, check path
```

### Exercise 2.2: Create and Delete
Create and delete files/folders.

```bash
# YOUR CODE HERE:
# mkdir, touch, rm, rmdir
```

### Exercise 2.3: Copy and Move
Copy and move files.

```bash
# YOUR CODE HERE:
# cp, mv commands
```

### Exercise 2.4: View File Contents
View file contents using different methods.

```bash
# YOUR CODE HERE:
# cat, head, tail, less
```

### Exercise 2.5: Search in Files
Search for patterns in files.

```bash
# YOUR CODE HERE:
# grep, grep -r, grep -i
```

### Exercise 2.6: Count Lines and Words
Count lines, words in a file.

```bash
# YOUR CODE HERE:
# wc -l, wc -w
```

### Exercise 2.7: Extract Columns
Extract specific columns from CSV.

```bash
# YOUR CODE HERE:
# awk, cut commands
```

### Exercise 2.8: Sort and Unique
Sort and find unique values.

```bash
# YOUR CODE HERE:
# sort, uniq commands
```

### Exercise 2.9: Change Permissions
Change file permissions.

```bash
# YOUR CODE HERE:
# chmod 755, chmod +x
```

### Exercise 2.10: Environment Variables
Set and use environment variables.

```bash
# YOUR CODE HERE:
# export, echo $VAR
```

### Exercise 2.11: Pipes and Redirection
Use pipes and redirection.

```bash
# YOUR CODE HERE:
# >, >>, | commands
```

### Exercise 2.12: Process Management
View and manage processes.

```bash
# YOUR CODE HERE:
# ps, top, kill commands
```

---

## Exercise Set 3: REST APIs

### Exercise 3.1: GET Request
Make a GET request using curl.

```bash
# YOUR CODE HERE:
# curl https://jsonplaceholder.typicode.com/users
```

### Exercise 3.2: POST Request
Make a POST request with JSON body.

```bash
# YOUR CODE HERE:
# Create new user via API
```

### Exercise 3.3: PUT Request
Update data using PUT.

```bash
# YOUR CODE HERE:
# Update user via API
```

### Exercise 3.4: DELETE Request
Delete data using DELETE.

```bash
# YOUR CODE HERE:
# Delete user via API
```

### Exercise 3.5: Python GET Request
Fetch data using Python requests.

```python
# YOUR CODE HERE:
import requests

# Fetch users from API
response = requests.get("https://jsonplaceholder.typicode.com/users")
# Print first user name
```

### Exercise 3.6: Python POST Request
Send data using Python.

```python
# YOUR CODE HERE:
# Create new post via API
```

### Exercise 3.7: Handle API Errors
Add error handling to API calls.

```python
# YOUR CODE HERE:
# Try/except, check status code
```

### Exercise 3.8: API Authentication
Make authenticated API request.

```python
# YOUR CODE HERE:
# Use API key or Bearer token
```

### Exercise 3.9: Parse JSON Response
Parse and extract data from JSON.

```python
# YOUR CODE HERE:
# Parse response, extract specific fields
```

### Exercise 3.10: Handle Rate Limiting
Implement retry logic for rate limits.

```python
# YOUR CODE HERE:
# Add retry with backoff
```

---

## Exercise Set 4: Networking Basics

### Exercise 4.1: Check IP Address
Check your machine's IP address.

```bash
# YOUR CODE HERE:
# ip addr, hostname -I
```

### Exercise 4.2: Test Connectivity
Test connection to a server.

```bash
# YOUR CODE HERE:
# ping, nc commands
```

### Exercise 4.3: Check DNS
Resolve domain name.

```bash
# YOUR CODE HERE:
# nslookup, dig commands
```

### Exercise 4.4: SSH Connection
Connect to remote server.

```bash
# YOUR CODE HERE:
# ssh commands
```

### Exercise 4.5: SCP File Transfer
Copy file to remote server.

```bash
# YOUR CODE HERE:
# scp command
```

### Exercise 4.6: Check Open Ports
List open ports on system.

```bash
# YOUR CODE HERE:
# netstat, ss commands
```

---

## Exercise Set 5: Data Formats

### Exercise 5.1: Read JSON
Parse JSON file in Python.

```python
# YOUR CODE HERE:
import json

# Read and parse data.json
```

### Exercise 5.2: Write JSON
Write data to JSON file.

```python
# YOUR CODE HERE:
# Create dict and write to file
```

### Exercise 5.3: Read CSV
Read CSV file using csv module.

```python
# YOUR CODE HERE:
import csv

# Read data.csv
```

### Exercise 5.4: Write CSV
Write data to CSV file.

```python
# YOUR CODE HERE:
# Create and write to output.csv
```

### Exercise 5.5: Read Parquet
Read Parquet file using pandas.

```python
# YOUR CODE HERE:
import pandas as pd

# Read data.parquet
```

### Exercise 5.6: Write Parquet
Write DataFrame to Parquet.

```python
# YOUR CODE HERE:
# Write to parquet format
```

### Exercise 5.7: Parse XML
Parse XML file in Python.

```python
# YOUR CODE HERE:
import xml.etree.ElementTree as ET

# Parse sample.xml
```

### Exercise 5.8: Convert CSV to JSON
Convert CSV data to JSON format.

```python
# YOUR CODE HERE:
# Read CSV, convert to JSON
```

---

## Exercise Set 6: Cloud Fundamentals

### Exercise 6.1: AWS CLI Setup
Configure AWS credentials.

```bash
# YOUR CODE HERE:
# aws configure
```

### Exercise 6.2: S3 Operations
List and manage S3 buckets.

```bash
# YOUR CODE HERE:
# aws s3 ls, cp, mb commands
```

### Exercise 6.3: EC2 Basics
List EC2 instances.

```bash
# YOUR CODE HERE:
# aws ec2 describe-instances
```

### Exercise 6.4: IAM User
Create IAM user and get credentials.

```bash
# YOUR CODE HERE:
# aws iam create-user
```

### Exercise 6.5: Azure CLI
List Azure resources.

```bash
# YOUR CODE HERE:
# az vm list, az storage account list
```

### Exercise 6.6: GCP Basics
List GCP resources.

```bash
# YOUR CODE HERE:
# gcloud compute instances list
```

---

## Exercise Set 7: Docker Basics

### Exercise 7.1: Pull Image
Pull a Docker image.

```bash
# YOUR CODE HERE:
# docker pull python:3.9
```

### Exercise 7.2: Run Container
Run a container.

```bash
# YOUR CODE HERE:
# docker run hello-world
```

### Exercise 7.3: List Containers
List running containers.

```bash
# YOUR CODE HERE:
# docker ps, docker ps -a
```

### Exercise 7.4: Stop and Remove
Stop and remove containers.

```bash
# YOUR CODE HERE:
# docker stop, docker rm
```

### Exercise 7.5: Build Dockerfile
Build image from Dockerfile.

```bash
# YOUR CODE HERE:
# docker build -t myapp .
```

### Exercise 7.6: Run with Volume
Run container with volume mount.

```bash
# YOUR CODE HERE:
# docker run -v /host:/container
```

### Exercise 7.7: Docker Compose
Start services with docker-compose.

```bash
# YOUR CODE HERE:
# docker-compose up -d
```

### Exercise 7.8: View Logs
View container logs.

```bash
# YOUR CODE HERE:
# docker logs container_id
```

---

## Exercise Set 8: Orchestration Basics

### Exercise 8.1: Create Cron Job
Schedule a cron job.

```bash
# YOUR CODE HERE:
# crontab -e
# Add job to run daily at midnight
```

### Exercise 8.2: List Cron Jobs
List scheduled cron jobs.

```bash
# YOUR CODE HERE:
# crontab -l
```

### Exercise 8.3: Python Scheduler
Use schedule library in Python.

```python
# YOUR CODE HERE:
import schedule
import time

# Schedule job to run hourly
def job():
    print("Running ETL job...")

schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
```

### Exercise 8.4: APScheduler
Use advanced Python scheduler.

```python
# YOUR CODE HERE:
from apscheduler.schedulers.blocking import BlockingScheduler

# Schedule daily job
```

---

## Exercise Set 9: SQL & Databases

### Exercise 9.1: SELECT Query
Write basic SELECT query.

```sql
-- YOUR CODE HERE:
-- Select all columns from customers
SELECT * FROM customers;
```

### Exercise 9.2: WHERE Clause
Filter results with WHERE.

```sql
-- YOUR CODE HERE:
-- Select customers from New York with age > 25
```

### Exercise 9.3: JOIN Tables
Join two tables together.

```sql
-- YOUR CODE HERE:
-- Join orders with customers
```

### Exercise 9.4: GROUP BY
Group and aggregate data.

```sql
-- YOUR CODE HERE:
-- Count orders by customer
```

### Exercise 9.5: ORDER BY
Sort results.

```sql
-- YOUR CODE HERE:
-- Sort by sales amount descending
```

### Exercise 9.6: INSERT Data
Insert new records.

```sql
-- YOUR CODE HERE:
-- Insert new customer
```

### Exercise 9.7: UPDATE Data
Update existing records.

```sql
-- YOUR CODE HERE:
-- Update customer email
```

### Exercise 9.8: DELETE Data
Delete records.

```sql
-- YOUR CODE HERE:
-- Delete old orders
```

### Exercise 9.9: Create Index
Create index for performance.

```sql
-- YOUR CODE HERE:
-- Create index on customer_id
```

### Exercise 9.10: CTE Query
Use Common Table Expression.

```sql
-- YOUR CODE HERE:
-- Write CTE for sales analysis
```

---

## Exercise Set 10: Scripting Basics

### Exercise 10.1: Bash Script
Create basic bash script.

```bash
#!/bin/bash

# YOUR CODE HERE:
# Script to backup files
```

### Exercise 10.2: Bash Variables
Use variables in bash.

```bash
#!/bin/bash

# YOUR CODE HERE:
# Create script with variables
```

### Exercise 10.3: Bash Conditionals
Use if/else in bash.

```bash
#!/bin/bash

# YOUR CODE HERE:
# Check if file exists
```

### Exercise 10.4: Bash Loop
Use for loop in bash.

```bash
#!/bin/bash

# YOUR CODE HERE:
# Loop through CSV files
```

### Exercise 10.5: Python Arguments
Parse command line arguments.

```python
#!/usr/bin/env python3
import argparse

# YOUR CODE HERE:
# Add --input, --output arguments
```

### Exercise 10.6: Python File Operations
Read and write files.

```python
# YOUR CODE HERE:
# Read file, process, write output
```

### Exercise 10.7: Python Error Handling
Add try/except handling.

```python
# YOUR CODE HERE:
# Handle file not found error
```

---

## Exercise Set 11: Security Basics

### Exercise 11.1: Environment Variables
Use environment variables for secrets.

```python
# YOUR CODE HERE:
import os

# Get API key from env var
```

### Exercise 11.2: .env File
Load variables from .env file.

```python
# YOUR CODE HERE:
from dotenv import load_dotenv

load_dotenv()
# Get secrets
```

### Exercise 11.3: Generate SSH Keys
Generate SSH key pair.

```bash
# YOUR CODE HERE:
# ssh-keygen -t ed25519
```

### Exercise 11.4: AWS Secrets
Retrieve secrets from AWS Secrets Manager.

```python
# YOUR CODE HERE:
import boto3

# Get secret from Secrets Manager
```

### Exercise 11.5: Hash Password
Hash password using hashlib.

```python
# YOUR CODE HERE:
import hashlib

# Hash a password
```

---

## Exercise Set 12: Monitoring & Logging

### Exercise 12.1: Basic Logging
Set up Python logging.

```python
# YOUR CODE HERE:
import logging

# Configure logging to file
logging.basicConfig(filename='app.log', level=logging.INFO)
logger = logging.getLogger(__name__)

# Log some messages
```

### Exercise 12.2: Health Check
Create health check function.

```python
# YOUR CODE HERE:
import requests

def check_service(url):
    # Check if service is healthy
    pass
```

### Exercise 12.3: Error Handling
Add proper error handling.

```python
# YOUR CODE HERE:
try:
    result = process_data()
except Exception as e:
    logger.error(f"Error: {e}")
```

### Exercise 12.4: Metrics Collection
Collect basic metrics.

```python
# YOUR CODE HERE:
# Track: requests processed, errors, latency
```

---

## Challenge Exercises

### Challenge 1: ETL Pipeline Script
Create a complete ETL script:
1. Read from API
2. Transform data
3. Write to CSV

```python
# YOUR CODE HERE:



```

### Challenge 2: Dockerized App
Create Dockerfile and docker-compose for a Python app.

```dockerfile
# YOUR CODE HERE:



```

### Challenge 3: Automated Backup
Create backup script with scheduling:
1. Backup database
2. Compress files
3. Upload to S3
4. Log status

```bash
#!/bin/bash
# YOUR CODE HERE:



```

---

## Testing Your Skills

### Quick Commands Reference

```bash
# Git
git status, git add ., git commit -m "msg", git push

# Linux
ls, cd, cp, mv, grep, wc, chmod

# Docker
docker ps, docker build, docker run, docker-compose

# Cloud
aws s3 ls, az vm list, gcloud compute list
```

---

## Practice Complete!

After completing these exercises, you should be comfortable with:
- Version control with Git
- Command line operations
- REST API consumption
- Basic networking
- Data format handling
- Cloud service basics
- Docker containerization
- Job scheduling
- SQL queries
- Scripting automation
- Security best practices
- Monitoring and logging

---

## Next Steps

1. Practice with real projects
2. Build automation scripts
3. Deploy applications with Docker
4. Set up monitoring for your pipelines
5. Learn more cloud services
