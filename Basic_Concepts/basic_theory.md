# Basic Concepts Theory for Data Engineering

This file provides essential theory explanations for fundamental skills that every data engineer needs. Each section includes practical explanations and code examples - focused on what's actually needed for daily work.

## Table of Contents
1. [Version Control with Git](#1-version-control-with-git)
2. [Command Line \& Linux Essentials](#2-command-line--linux-essentials)
3. [REST APIs](#3-rest-apis)
4. [Networking Basics](#4-networking-basics)
5. [Data Formats](#5-data-formats)
6. [Cloud Fundamentals](#6-cloud-fundamentals)
7. [Container Basics (Docker)](#7-container-basics-docker)
8. [Orchestration Basics](#8-orchestration-basics)
9. [SQL \& Databases](#9-sql--databases)
10. [Scripting Basics](#10-scripting-basics)
11. [Security Basics](#11-security-basics)
12. [Monitoring \& Logging](#12-monitoring--logging)

---

## 1. Version Control with Git

### 📖 What is Git?

**Git** is a distributed version control system that tracks changes in your code. It allows multiple people to work on the same project, manage versions, and collaborate effectively.

**Why is this important for Data Engineering?**

- Track changes in ETL pipelines and data models
- Collaborate with team members
- Maintain code history and rollback when needed
- Branch for development and testing

### Basic Git Commands

```bash
# Initialize a new repository
git init

# Clone an existing repository
git clone https://github.com/user/repo.git

# Check status
git status

# Add files to staging
git add filename.txt
git add .                    # Add all files

# Commit changes
git commit -m "Commit message"

# View history
git log
git log --oneline            # Compact view

# View differences
git diff                     # Unstaged changes
git diff --staged           # Staged changes
```

### Branching and Merging

```bash
# Create and switch to new branch
git checkout -b feature/new-branch

# Switch branches
git checkout main
git checkout branch-name

# List branches
git branch
git branch -a               # All branches

# Merge branch into current
git merge feature-branch

# Delete branch
git branch -d branch-name   # Local delete
git push origin --delete remote-branch  # Remote delete
```

### Remote Operations

```bash
# Add remote
git remote add origin https://github.com/user/repo.git

# Push to remote
git push origin main
git push -u origin feature-branch   # -u sets upstream

# Pull from remote
git pull origin main

# Fetch updates
git fetch origin
```

### Handling Merge Conflicts

```bash
# When merge conflict occurs:
# 1. Edit the conflicted files
# 2. Remove conflict markers (<<<<<<<, =======, >>>>>>>)
# 3. Add resolved files
git add filename.py
git commit -m "Resolved merge conflict"
```

### GitHub Workflow

```bash
# Typical workflow
# 1. Fork repository (on GitHub)
# 2. Clone your fork
git clone https://github.com/yourusername/repo.git

# 3. Create feature branch
git checkout -b feature/my-feature

# 4. Make changes and commit
git add .
git commit -m "Add new feature"

# 5. Push to your fork
git push origin feature/my-feature

# 6. Create Pull Request (on GitHub)
# 7. Review and merge
```

### .gitignore

```bash
# .gitignore example

# Python
__pycache__/
*.py[cod]
*$py.class
*.egg-info/
venv/
.env

# Data files
*.csv
*.parquet
*.db
data/

# IDE
.vscode/
.idea/
*.swp

# Logs
*.log

# OS
.DS_Store
Thumbs.db
```

---

## 2. Command Line & Linux Essentials

### 📖 Why is Command Line Important?

**Command Line** allows you to interact with your computer using text commands. Data engineers use it extensively for file manipulation, data processing, and server management.

**Why is this important for Data Engineering?**

- Process large files efficiently
- Automate repetitive tasks
- Manage servers and cloud resources
- Run ETL pipelines and scripts

### File Operations

```bash
# Navigation
ls                      # List files
ls -la                  # Detailed list with hidden files
ls -lh                  # Human-readable sizes
cd directory            # Change directory
cd ..                   # Go back
cd ~                    # Go home
pwd                     # Print working directory

# Create/Delete
mkdir newfolder         # Create directory
rmdir folder           # Remove empty directory
rm file.txt            # Delete file
rm -rf folder          # Delete folder (recursive force)

# Copy/Move
cp source.txt dest.txt
cp -r folder/ newfolder/
mv oldname.txt newname.txt
mv file.txt folder/
```

### File Viewing

```bash
# View file contents
cat file.txt            # Show entire file
head -n 10 file.txt    # First 10 lines
tail -n 10 file.txt    # Last 10 lines
less file.txt           # Paginated view (q to quit)

# Watch file updates
tail -f logfile.log    # Follow log file
```

### Text Processing

```bash
# Search in files
grep "pattern" file.txt         # Find pattern
grep -r "pattern" folder/      # Recursive search
grep -i "pattern" file.txt     # Case insensitive
grep -n "pattern" file.txt     # Show line numbers

# Count lines/words
wc -l file.txt                 # Count lines
wc -w file.txt                 # Count words

# Extract columns
awk -F',' '{print $1}' file.csv   # Print 1st column
cut -d',' -f1,3 file.csv          # Multiple columns

# Sort
sort file.txt                  # Sort lines
sort -u file.txt               # Sort and remove duplicates
sort -k2 file.txt              # Sort by 2nd column

# Find unique
uniq file.txt                  # Remove adjacent duplicates
```

### Permissions

```bash
# Permission basics (rwxr-xr-x)
# Owner | Group | Others
# r=4, w=2, x=1

# Change permissions
chmod 755 script.sh           # rwx r-x r-x
chmod +x script.sh            # Add execute
chmod -R 777 folder/          # Full access

# Change owner
chown user:group file.txt
```

### Environment Variables

```bash
# View variables
echo $PATH
env

# Set variable (temporary)
export VARIABLE_NAME="value"

# Set variable (persistent) - add to ~/.bashrc
echo 'export MY_VAR="value"' >> ~/.bashrc
source ~/.bashrc
```

### Pipes and Redirection

```bash
# Redirect output
command > file.txt            # Overwrite
command >> file.txt           # Append
command 2> error.txt         # Error only

# Pipes
cat file.txt | grep "pattern" | wc -l
ls -l | grep "pattern"
head -100 file.txt | tail -10

# Combining
command > output.txt 2>&1     # Both stdout and stderr
```

### Process Management

```bash
# View processes
ps                           # Current shell processes
ps aux                       # All processes
top                          # Interactive process viewer

# Kill process
kill process_id
kill -9 process_id           # Force kill

# Background processes
command &                    # Run in background
jobs                         # List background jobs
Ctrl+Z                       # Suspend current job
bg                           # Resume in background
fg                           # Bring to foreground
```

### Package Managers

```bash
# Ubuntu/Debian
apt update
apt install package-name
apt remove package-name

# Python packages
pip install package-name
pip install -r requirements.txt

# Node packages
npm install package-name
```

---

## 3. REST APIs

### 📖 What is a REST API?

**REST (Representational State Transfer) API** is a way for applications to communicate over HTTP. It uses standard HTTP methods to perform operations on data.

**Why is this important for Data Engineering?**

- Fetch data from external services
- Integrate with third-party APIs
- Build data pipelines that pull/push data
- Automate workflows

### HTTP Methods

| Method | Purpose | Example |
|--------|---------|---------|
| **GET** | Retrieve data | Get all users |
| **POST** | Create new data | Create new user |
| **PUT** | Replace data | Update entire user |
| **PATCH** | Partial update | Update user email |
| **DELETE** | Remove data | Delete user |

### HTTP Status Codes

| Code | Meaning |
|------|---------|
| **200** | OK - Success |
| **201** | Created - Resource created |
| **400** | Bad Request - Invalid input |
| **401** | Unauthorized - Need authentication |
| **403** | Forbidden - No permission |
| **404** | Not Found - Resource doesn't exist |
| **429** | Too Many Requests - Rate limited |
| **500** | Server Error |

### Making API Requests

```bash
# GET request
curl https://api.example.com/users
curl -X GET "https://api.example.com/users?id=123"

# POST request
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "email": "john@example.com"}'

# PUT request
curl -X PUT https://api.example.com/users/123 \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe"}'

# DELETE request
curl -X DELETE https://api.example.com/users/123
```

### Using APIs with Python

```python
import requests

# GET request
response = requests.get("https://api.example.com/users")
print(response.status_code)
data = response.json()

# POST request
payload = {"name": "John", "email": "john@example.com"}
response = requests.post(
    "https://api.example.com/users",
    json=payload
)

# Headers
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}
response = requests.get(
    "https://api.example.com/data",
    headers=headers
)

# Error handling
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raise for bad status
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

### Authentication

```python
# API Key
headers = {"X-API-Key": "your-api-key"}
response = requests.get(url, headers=headers)

# Bearer Token (OAuth)
headers = {"Authorization": "Bearer YOUR_TOKEN"}
response = requests.get(url, headers=headers)

# Basic Auth
from requests.auth import HTTPBasicAuth
response = requests.get(
    url,
    auth=HTTPBasicAuth("username", "password")
)
```

### Handling Rate Limiting

```python
import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Retry strategy
session = requests.Session()
retry = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504]
)
adapter = HTTPAdapter(max_retries=retry)
session.mount("http://", adapter)
session.mount("https://", adapter)

# Check rate limit headers
response = requests.get(url)
remaining = response.headers.get("X-RateLimit-Remaining")
print(f"API calls remaining: {remaining}")
```

---

## 4. Networking Basics

### 📖 Why is Networking Important?

**Networking** basics help data engineers connect to databases, access cloud services, and troubleshoot connectivity issues.

**Why is this important for Data Engineering?**

- Connect to databases and cloud services
- Set up SSH tunnels
- Configure firewalls
- Debug connection issues

### IP Addresses

```bash
# IPv4 format: x.x.x.x (0-255 each)
# Example: 192.168.1.1

# Private IP ranges:
# 10.0.0.0 - 10.255.255.255
# 172.16.0.0 - 172.31.255.255
# 192.168.0.0 - 192.168.255.255

# Check IP address
ip addr
hostname -I
```

### Common Ports

| Port | Service | Use Case |
|------|---------|----------|
| 22 | SSH | Secure remote access |
| 80 | HTTP | Web traffic |
| 443 | HTTPS | Secure web traffic |
| 3306 | MySQL | MySQL database |
| 5432 | PostgreSQL | PostgreSQL database |
| 6379 | Redis | Redis cache |
| 8080 | HTTP Alt | Development servers |
| 27017 | MongoDB | MongoDB database |

### SSH Basics

```bash
# Connect to server
ssh username@server-ip
ssh -i key.pem username@server-ip    # With key

# SSH key generation
ssh-keygen -t rsa -b 4096

# Copy public key to server
ssh-copy-id username@server-ip

# SSH tunnel (port forwarding)
ssh -L 5432:localhost:5432 user@remote-server
```

### DNS Basics

```bash
# Check DNS resolution
nslookup example.com
dig example.com
host example.com

# Flush DNS cache (Ubuntu)
sudo systemd-resolve --flush-caches
```

### Testing Connectivity

```bash
# Ping server
ping example.com

# Check port connectivity
nc -zv example.com 443
telnet example.com 22

# Trace route
traceroute example.com

# Check open ports
netstat -tulpn
ss -tulpn
```

---

## 5. Data Formats

### 📖 Why are Data Formats Important?

**Data formats** define how data is stored and structured. Understanding different formats helps you choose the right one for your use case.

**Why is this important for Data Engineering?**

- Choose efficient formats for storage
- Parse various data types
- Optimize for performance
- Handle nested data

### JSON (JavaScript Object Notation)

```python
import json

# Parse JSON
json_string = '{"name": "John", "age": 30, "skills": ["Python", "SQL"]}'
data = json.loads(json_string)

# Access nested data
print(data["name"])                    # John
print(data["skills"][0])              # Python

# Create JSON
data = {
    "name": "Jane",
    "age": 25,
    "address": {
        "city": "NYC",
        "zip": "10001"
    }
}
json_string = json.dumps(data, indent=2)

# Read from file
with open("data.json", "r") as f:
    data = json.load(f)

# Write to file
with open("output.json", "w") as f:
    json.dump(data, f, indent=2)
```

### CSV (Comma-Separated Values)

```python
import csv

# Read CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Read CSV with headers
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["email"])

# Write CSV
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Email"])
    writer.writerow(["John", "john@example.com"])

# Using pandas (more powerful)
import pandas as pd
df = pd.read_csv("data.csv")
df.to_csv("output.csv", index=False)
```

### Parquet (Columnar Format)

```python
import pandas as pd

# Read Parquet
df = pd.read_parquet("data.parquet")

# Write Parquet
df.to_parquet("output.parquet", engine="pyarrow")

# Read specific columns
df = pd.read_parquet("data.parquet", columns=["name", "age"])
```

### XML Basics

```python
import xml.etree.ElementTree as ET

# Parse XML
xml_string = """<?xml version="1.0"?>
<users>
    <user id="1">
        <name>John</name>
        <email>john@example.com</email>
    </user>
</users>"""

root = ET.fromstring(xml_string)

# Access elements
for user in root.findall("user"):
    print(user.get("id"))
    print(user.find("name").text)

# Create XML
root = ET.Element("users")
user = ET.SubElement(root, "user", id="1")
name = ET.SubElement(user, "name")
name.text = "John"

xml_str = ET.tostring(root, encoding="unicode")
```

---

## 6. Cloud Fundamentals

### 📖 Why is Cloud Important?

**Cloud platforms** provide infrastructure and services for storing, processing, and analyzing data at scale.

**Why is this important for Data Engineering?**

- Host data pipelines
- Store large datasets
- Use managed database services
- Scale compute resources

### Key Concepts

```bash
# Virtual Machines (VMs)
# - Scalable computing resources
# - You manage OS and software
# - Use case: Custom requirements

# Storage
# - Object storage (S3, Blob): Files, data lakes
# - Block storage: VM disks
# - File storage: Shared file systems

# Networking
# - VPC: Virtual network
# - Subnet: Subdivision of VPC
# - Security groups: Firewall rules
```

### IAM (Identity and Access Management)

```bash
# IAM Best Practices
# - Use least privilege principle
# - Enable MFA for users
# - Use roles, not access keys
# - Rotate credentials regularly
# - Never commit keys to git
```

### Common Services (AWS Example)

| Service | Purpose |
|---------|---------|
| S3 | Object storage |
| EC2 | Virtual machines |
| RDS | Managed databases |
| Lambda | Serverless functions |
| Glue | ETL service |
| Redshift | Data warehouse |
| Athena | Query S3 with SQL |

---

## 7. Container Basics (Docker)

### 📖 What is Docker?

**Docker** is a platform for containerization - packaging applications with their dependencies into portable containers.

**Why is this important for Data Engineering?**

- Consistent environments
- Easy deployment
- Resource isolation
- Reproducible pipelines

### Basic Docker Commands

```bash
# Run a container
docker run hello-world
docker run -it python:3.9 bash    # Interactive terminal

# Common options
-d          # Detached (background)
-p 8080:80  # Port mapping (host:container)
-v /data:/data  # Volume mount
-e VAR=value    # Environment variable
--name mycontainer  # Container name

# Manage containers
docker ps                 # Running containers
docker ps -a             # All containers
docker stop container_id
docker rm container_id

# Manage images
docker images
docker rmi image_name
docker pull python:3.9
```

### Dockerfile

```dockerfile
# Dockerfile example for Python app
FROM python:3.9-slim

WORKDIR /app

# Copy requirements first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Environment variables
ENV PYTHONUNBUFFERED=1

# Run application
CMD ["python", "app.py"]
```

### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DB_HOST=postgres
    depends_on:
      - postgres
      - redis

  postgres:
    image: postgres:14
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data

  redis:
    image: redis:7

volumes:
  pgdata:
```

```bash
# Docker Compose commands
docker-compose up -d          # Start all services
docker-compose down           # Stop all services
docker-compose logs -f        # View logs
docker-compose ps            # Status
```

---

## 8. Orchestration Basics

### 📖 What is Orchestration?

**Orchestration** involves automating the execution of tasks in a coordinated manner, often on a schedule.

**Why is this important for Data Engineering?**

- Schedule ETL jobs
- Manage dependencies
- Handle failures
- Monitor pipelines

### Cron Jobs

```bash
# Cron syntax
# * * * * * command
# | | | | |
# | | | | +--- Day of week (0-7, 0 and 7 are Sunday)
# | | | +----- Month (1-12)
# | | +------- Day of month (1-31)
# | +--------- Hour (0-23)
# +----------- Minute (0-59)

# Examples
0 * * * *          # Every hour
0 0 * * *          # Daily at midnight
0 0 * * 0          # Weekly on Sunday
0 */6 * * *        # Every 6 hours

# Edit crontab
crontab -e

# List crontab
crontab -l
```

### Basic Workflow Concepts

```python
# Simple scheduler in Python
import schedule
import time

def job():
    print("Running ETL job...")

# Schedule jobs
schedule.every().hour.do(job)
schedule.every().day.at("10:00").do(job)
schedule.every().monday.at("09:00").do(job)

# Run scheduler
while True:
    schedule.run_pending()
    time.sleep(60)
```

---

## 9. SQL & Databases

### 📖 Why is SQL Important?

**SQL (Structured Query Language)** is the standard language for interacting with databases - essential for any data professional.

**Why is this important for Data Engineering?**

- Query data from databases
- Write ETL transformations
- Create data models
- Optimize performance

### Basic Queries

```sql
-- SELECT basics
SELECT column1, column2
FROM table_name;

SELECT * FROM table_name;

-- Filtering
WHERE age > 25
  AND city = 'NYC';

-- Sorting
ORDER BY column1 ASC, column2 DESC;

-- Limit results
LIMIT 10;

-- Aggregations
SELECT
    COUNT(*) as total,
    SUM(amount) as total_amount,
    AVG(price) as avg_price,
    MIN(date) as earliest,
    MAX(date) as latest
FROM sales;

-- Grouping
SELECT category, SUM(sales) as total_sales
FROM products
GROUP BY category
HAVING SUM(sales) > 1000;
```

### JOINs

```sql
-- INNER JOIN - Only matching rows
SELECT *
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id;

-- LEFT JOIN - All from left, matching from right
SELECT *
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id;

-- Multiple JOINs
SELECT
    o.order_id,
    c.name,
    p.product_name,
    oi.quantity
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.id;
```

### Subqueries and CTEs

```sql
-- Subquery in WHERE
SELECT *
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- CTE (Common Table Expression)
WITH regional_sales AS (
    SELECT region, SUM(amount) AS total_sales
    FROM orders
    GROUP BY region
), top_regions AS (
    SELECT region
    FROM regional_sales
    WHERE total_sales > (SELECT SUM(total_sales)/10 FROM regional_sales)
)
SELECT region, product, SUM(quantity) AS product_units, SUM(amount) AS product_sales
FROM orders
WHERE region IN (SELECT region FROM top_regions)
GROUP BY region, product;
```

### Indexes

```sql
-- Create index
CREATE INDEX idx_customer_name ON customers(name);

-- Composite index
CREATE INDEX idx_order_date_customer ON orders(order_date, customer_id);

-- Unique index
CREATE UNIQUE INDEX idx_user_email ON users(email);

-- View indexes
SELECT * FROM pg_indexes WHERE tablename = 'orders';
```

---

## 10. Scripting Basics

### 📖 Why is Scripting Important?

**Scripting** helps automate repetitive tasks and build data pipelines.

**Why is this important for Data Engineering?**

- Automate data processing
- Build ETL pipelines
- Handle file operations
- Integrate systems

### Bash Scripting Basics

```bash
#!/bin/bash

# Variables
NAME="John"
echo "Hello, $NAME"

# Command output
CURRENT_DATE=$(date +%Y-%m-%d)
echo "Today is $CURRENT_DATE"

# Conditionals
if [ $AGE -gt 18 ]; then
    echo "Adult"
else
    echo "Minor"
fi

# Loops
for file in *.csv; do
    echo "Processing $file"
done

# Arguments
echo "First argument: $1"
echo "All arguments: $@"
```

### Python Scripting

```python
#!/usr/bin/env python3

import os
import sys
import argparse
from pathlib import Path

# Parse arguments
parser = argparse.ArgumentParser(description="Process data files")
parser.add_argument("--input", required=True, help="Input file")
parser.add_argument("--output", help="Output file")
args = parser.parse_args()

# Work with files
input_path = Path(args.input)
if input_path.exists():
    with open(input_path, 'r') as f:
        data = f.read()

# Exit with status
sys.exit(0)  # Success
sys.exit(1)  # Error

# Error handling
try:
    result = process_data(data)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
```

---

## 11. Security Basics

### 📖 Why is Security Important?

**Security** protects sensitive data and systems from unauthorized access.

**Why is this important for Data Engineering?**

- Protect credentials
- Secure data pipelines
- Comply with regulations
- Prevent breaches

### Environment Variables

```bash
# Set environment variable
export DATABASE_URL="postgresql://user:pass@host/db"
export API_KEY="your-api-key"

# In Python
import os
db_url = os.environ.get("DATABASE_URL")
api_key = os.environ.get("API_KEY")
```

### .env Files

```bash
# .env file (add to .gitignore!)
DATABASE_URL=postgresql://user:pass@localhost/db
API_KEY=your-api-key
AWS_SECRET_ACCESS_KEY=your-secret
```

```python
# Using python-dotenv
from dotenv import load_dotenv
load_dotenv()  # Loads .env file

import os
api_key = os.getenv("API_KEY")
```

### SSH Keys

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add to ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key to server
ssh-copy-id user@server
```

### Secrets Management

```python
# For cloud (AWS Secrets Manager example)
import boto3
import json

client = boto3.client('secretsmanager')
response = client.get_secret_value(SecretId='my-database-password')
secret = json.loads(response['SecretString'])
password = secret['password']
```

---

## 12. Monitoring & Logging

### 📖 Why is Monitoring Important?

**Monitoring and logging** help track system health, debug issues, and ensure reliable data pipelines.

**Why is this important for Data Engineering?**

- Debug pipeline failures
- Track data quality
- Alert on errors
- Optimize performance

### Basic Logging in Python

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Use logging
logger.info("Processing started")
logger.warning("Missing data in row 5")
logger.error("Failed to connect to database")
logger.debug("Variable value: x")
```

### Health Checks

```python
import requests
from datetime import datetime

def check_api_health(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
    except:
        return False
    return False

# Check database
def check_database_connection():
    import psycopg2
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="mydb",
            user="user",
            password="pass"
        )
        conn.close()
        return True
    except:
        return False
```

### Error Handling

```python
# Best practices for data pipelines

# Wrap critical operations
try:
    result = process_data(input_file)
except FileNotFoundError:
    logger.error(f"Input file not found: {input_file}")
    # Send alert, use fallback, etc.
except Exception as e:
    logger.exception("Unexpected error")
    raise  # Re-raise if can't handle

# Always clean up
try:
    process_data()
finally:
    cleanup_resources()

# Context managers for resources
with open('file.txt', 'r') as f:
    data = f.read()
# File automatically closed
```

---

## Quick Reference

### Essential Commands Summary

| Task | Command |
|------|---------|
| List files | `ls -la` |
| Find in file | `grep -r "pattern" .` |
| Check disk space | `df -h` |
| Check memory | `free -h` |
| Kill process | `kill -9 PID` |
| SSH with key | `ssh -i key.pem user@host` |
| Copy remote | `scp file user@host:/path` |
| Check port | `nc -zv host port` |

### Common Error Codes

| Code | Meaning |
|------|---------|
| 127 | Command not found |
| 1 | General error |
| 2 | Misuse of command |
| 13 | Permission denied |
| 116 | Stale file handle |

---

**Remember: Focus on practical skills - you don't need to be a Linux expert or network engineer, just know enough to get your data engineering work done!**
