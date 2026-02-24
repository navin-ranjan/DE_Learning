# Apache Airflow Theory & Quick Review Notes

## Table of Contents
1. [Airflow Fundamentals](#1-airflow-fundamentals)
2. [Airflow Architecture](#2-airflow-architecture)
3. [DAG Fundamentals](#3-dag-fundamentals)
4. [Scheduling Deep Dive](#4-scheduling-deep-dive)
5. [Operators](#5-operators)
6. [Sensors & Deferrable Operators](#6-sensors--deferrable-operators)
7. [TaskFlow API](#7-taskflow-api)
8. [XCom](#8-xcom)
9. [Variables, Connections & Hooks](#9-variables-connections--hooks)
10. [Executors & Scaling](#10-executors--scaling)
11. [Reliability, Backfill & Recovery](#11-reliability-backfill--recovery)
12. [Security](#12-security)
13. [Monitoring & Observability](#13-monitoring--observability)
14. [Cloud Integrations](#14-cloud-integrations)
15. [Best Practices](#15-best-practices)
16. [Top Review Questions (Ready Answers)](#16-top-review-questions-ready-answers)
17. [One-Click Revision Sheet](#17-one-click-revision-sheet)

---

## 1. Airflow Fundamentals

### 📖 What is Apache Airflow?

Apache Airflow is an open-source **workflow orchestrator** used to schedule, monitor, and manage data pipelines.

**Core idea:**
- Airflow controls **when** tasks run and **in what order**.
- External systems (Spark, dbt, BigQuery, etc.) do heavy processing.

**Why important for Data Engineering?**
- Automates ETL/ELT pipelines
- Provides retries, alerts, and dependency control
- Enables code-based pipelines with version control

### Orchestration vs Processing

| Concept | Meaning | Example |
|---------|---------|---------|
| Orchestration | Controls workflow execution | Trigger Spark job, wait, then load |
| Processing | Does heavy compute/transformation | Spark SQL aggregation on 1TB data |

**Key line:**
"Airflow should orchestrate compute, not become the compute engine."

---

## 2. Airflow Architecture

### 📖 Main Components

| Component | Role |
|-----------|------|
| Webserver | UI for DAGs, runs, logs, admin actions |
| Scheduler | Decides which tasks should run and when |
| Executor | Decides where runnable tasks execute |
| Worker | Actually runs task code |
| Metadata DB | Stores DAG runs, task states, XComs, configs |
| Triggerer | Handles deferrable async waiting tasks |

### How execution happens (simple flow)
1. Scheduler parses DAG files.
2. Scheduler creates DAG Runs and Task Instances.
3. Executor sends tasks to workers.
4. Workers execute and update status in metadata DB.
5. Webserver reads DB and shows UI state.

**Key focus:**
If metadata DB is slow/unhealthy, scheduler and UI both suffer.

---

## 3. DAG Fundamentals

### 📖 What is a DAG?

DAG = **Directed Acyclic Graph**
- Directed: task order matters (`A >> B`)
- Acyclic: no loops/cycles allowed

### Key DAG terms

| Term | Meaning |
|------|---------|
| DAG | Pipeline definition |
| DAG Run | One execution of DAG for a specific data interval |
| Task | Single unit of work |
| Task Instance | A task in one specific DAG run |

### Important DAG parameters

```python
with DAG(
    dag_id="daily_orders_etl",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["etl", "orders"]
):
    ...
```

- `start_date`: first logical scheduling boundary
- `schedule`: frequency (cron/preset/timetable)
- `catchup`: whether to create historical runs automatically

### Dependencies

```python
extract >> transform >> load
```

- `A >> B`: B waits for A
- `A << B`: A waits for B

---

## 4. Scheduling Deep Dive

### 📖 Logical Date and Data Interval

This is one of the most asked topics.

- Airflow schedules by **data interval**, not by current wall-clock only.
- A run may execute later, but should process the interval it represents.

**Example:**
Daily DAG run for `2026-02-22` can start on `2026-02-23`, but must process `2026-02-22` data.

### Cron and Presets

```python
schedule="0 2 * * *"   # 2 AM daily
schedule="@hourly"
schedule="@daily"
```

### Timetables
Use custom timetables when cron cannot express business calendar logic.

### Dataset Scheduling
Use dataset-based triggers for event-driven pipelines.

**Example:**
DAG B runs when DAG A updates dataset `s3://warehouse/sales/dt=...`.

### Trigger Rules

| Rule | Meaning |
|------|---------|
| `all_success` | Run only if all upstream succeeded (default) |
| `one_failed` | Run if any upstream failed |
| `all_done` | Run after all upstream finished in any final state |

---

## 5. Operators

### 📖 What is an Operator?

An operator defines *what to do* in a task.

| Operator | Use Case |
|----------|----------|
| `PythonOperator` | Python function execution |
| `BashOperator` | Shell command |
| `EmailOperator` | Send email alerts |
| `EmptyOperator` | No-op node for flow structure |
| `BranchPythonOperator` | Conditional branch selection |
| `ShortCircuitOperator` | Skip downstream if condition false |

### Example: PythonOperator

```python
def validate_count(**context):
    if context["ti"].xcom_pull(task_ids="extract") == 0:
        raise ValueError("No data extracted")
```

---

## 6. Sensors & Deferrable Operators

### 📖 What is a Sensor?

Sensor waits for an external condition before pipeline continues.

| Sensor | Waits for |
|--------|-----------|
| `FileSensor` | File path existence |
| `SqlSensor` | SQL query condition |
| `S3KeySensor` / GCS object sensor | Object availability |
| `ExternalTaskSensor` | Task/DAG completion in another DAG |
| `DateTimeSensor` | Specific datetime |

### `poke` vs `reschedule`

- `poke`: holds worker slot while waiting
- `reschedule`: releases worker between checks

### Deferrable Operators

Deferrable operators offload waiting to **Triggerer**, reducing worker usage.

**Key line:**
"For long waits, prefer deferrable or reschedule mode to avoid wasting worker slots."

---

## 7. TaskFlow API

### 📖 Why TaskFlow?

TaskFlow makes DAGs Pythonic and readable using decorators.

```python
from airflow.decorators import dag, task

@task
def extract():
    return [1, 2, 3]

@task
def transform(nums):
    return [n * 10 for n in nums]

@task
def load(nums):
    print(nums)

load(transform(extract()))
```

### Key Benefits
- Cleaner syntax
- Automatic XCom passing via return values
- Dependency inference from function calls

---

## 8. XCom

### 📖 What is XCom?

XCom (Cross-Communication) is Airflow's built-in mechanism to pass **small metadata** between tasks in the same DAG run.

Think of XCom as a message board for task-to-task coordination.

**Why is this important for Data Engineering?**
- Helps pass runtime values (for example, dynamic partition path)
- Enables dependent tasks to use upstream outputs
- Keeps DAG logic dynamic without hardcoding values

### How XCom works
- Upstream task pushes value (`xcom_push` or return value in TaskFlow).
- Downstream task pulls value (`xcom_pull`) using task id and optional key.
- Values are stored in metadata DB.

### Good use cases
- File path (`s3://bucket/sales/dt=2026-02-22/file.parquet`)
- Row count (`124532`)
- Generated run id / batch id
- Boolean status flag (`is_data_ready=True`)

### Bad use cases
- Full DataFrame
- CSV/Parquet binary payload
- MB/GB object blobs
- Anything large that can bloat metadata DB

### Example: Push and Pull in classic operators

```python
def extract(**context):
    output_path = "s3://raw/orders/dt=2026-02-22/orders.parquet"
    context["ti"].xcom_push(key="raw_path", value=output_path)

def transform(**context):
    raw_path = context["ti"].xcom_pull(task_ids="extract_task", key="raw_path")
    print(f"Reading file from: {raw_path}")
```

### Example: TaskFlow automatic XCom

```python
@task
def extract():
    return {"row_count": 1000, "path": "s3://raw/orders/dt=2026-02-22/"}

@task
def load(meta):
    print(meta["path"], meta["row_count"])

load(extract())
```

**Best practice:** Store actual data in S3/GCS/DB and pass only URI or ids in XCom.

---

## 9. Variables, Connections & Hooks

### 📖 What are Variables, Connections, and Hooks?

These three are often confused in practice. Each has a different purpose.

### Airflow Variables
Variables are global key-value config values.

**Use Variables for:**
- Feature flags
- Runtime thresholds
- Non-secret config

```python
from airflow.models import Variable

env_name = Variable.get("env_name", default_var="dev")
max_retry = int(Variable.get("max_retry_count", default_var="3"))
```

### Connections
Connections store endpoint + credentials securely for external systems.

**Examples of connection ids:**
- `postgres_dw`
- `aws_default`
- `gcp_bigquery_conn`

**Where to define:**
- Airflow UI
- CLI
- Environment variables
- Secrets backend (recommended for production)

```bash
export AIRFLOW_CONN_POSTGRES_DW='postgresql://user:pass@host:5432/dwh'
```

### Hooks
Hooks are Python wrappers/clients used to interact with external systems.

**Common hooks:**
- `PostgresHook`
- `S3Hook`
- `BigQueryHook`

```python
from airflow.providers.postgres.hooks.postgres import PostgresHook

hook = PostgresHook(postgres_conn_id="postgres_dw")
records = hook.get_records("SELECT COUNT(*) FROM fact_orders")
print(records)
```

### Quick difference

| Item | Scope | Purpose | Should hold secrets? |
|------|-------|---------|----------------------|
| Variables | Global | Runtime config | Usually no |
| Connections | Global/Secure | Endpoint + auth | Yes |
| XCom | Per DAG run | Small task messages | No |

**Quick tip:**
"Use Variables for config, Connections for credentials, XCom for run-time metadata between tasks."

---

## 10. Executors & Scaling

### 📖 Executor types

| Executor | Best For | Limitation |
|----------|----------|------------|
| `SequentialExecutor` | Local learning/testing | One task at a time |
| `LocalExecutor` | Single machine parallelism | Host-limited scale |
| `CeleryExecutor` | Distributed workers | Needs broker/backend ops |
| `KubernetesExecutor` | Per-task pod isolation, elastic scale | K8s operational complexity |

### Concurrency controls
- `parallelism`: max running task instances globally
- `max_active_runs` per DAG
- `max_active_tasks` per DAG (version-dependent features)
- task-level limits (for hot tasks)
- pools (resource protection)
- queues (route workload to specific worker groups)

**Example:**
Create pool `warehouse_writes` with 5 slots to protect database from overload.

```bash
airflow pools set warehouse_writes 5 "limit DW write concurrency"
```

### Choosing executor (practical)

| Scenario | Recommended Executor | Reason |
|----------|----------------------|--------|
| Learning / local laptop | `SequentialExecutor` or `LocalExecutor` | Simple setup |
| Small team, one VM | `LocalExecutor` | Easy parallelism |
| Medium/large distributed platform | `CeleryExecutor` | Queue-based horizontal scale |
| Cloud-native with strong isolation | `KubernetesExecutor` | Pod-level isolation and elasticity |

### Example answer
"At startup stage I use LocalExecutor for simplicity. As DAG count and concurrency grow, I move to CeleryExecutor. For strict multi-tenant isolation and elastic infra, KubernetesExecutor is preferred."

---

## 11. Reliability, Backfill & Recovery

### Retries and Timeouts

```python
default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "execution_timeout": timedelta(minutes=30)
}
```

### Idempotency (must-have)
Idempotency means rerunning the same task for the same interval gives the same final state.

**Patterns:**
- `MERGE`/`UPSERT`
- Partition overwrite
- Deterministic output path

### Catchup vs Backfill
- Catchup: scheduler auto-creates missing historical runs
- Backfill: manual historical run execution

### Failure states and retries (must-know)
- `up_for_retry`: task failed but retries remain
- `failed`: retries exhausted or hard failure
- `skipped`: intentionally not executed (branching/short-circuit)
- `upstream_failed`: blocked because upstream failed

### Recovery playbook
1. Identify failed interval and failed task.
2. Check partial writes.
3. Fix root cause.
4. Clear and rerun only required tasks/intervals.
5. Validate data quality post-recovery.

### Real-world recovery example
If `load_fact_orders` failed after inserting 40% data:
1. Confirm affected partition (`dt='2026-02-22'`).
2. Delete/overwrite only that partition.
3. Re-run transform + load for that date.
4. Compare counts with source before publishing success.

### Why this matters
Reliable recovery is what separates beginner pipelines from production-grade data platforms.

---

## 12. Security

### 📖 Why security matters in Airflow?

Airflow controls pipelines that often have warehouse, storage, and production credentials.  
If compromised, both data and infrastructure are at risk.

### Core Security Controls
- Authentication (LDAP/OAuth/SAML depending setup)
- Authorization (RBAC roles)
- Secrets backend (Vault / cloud secret managers)
- Least-privilege IAM and DB roles

### Secrets management pattern
- Keep secrets outside DAG code.
- Use Connections + Secrets Backend integration.
- Rotate credentials periodically.

### Security anti-patterns
- Hardcoded passwords in DAG code
- Shared admin account
- Over-privileged service users

### Key line
"In production, every DAG/service account should have least privilege and secrets must come from a managed secrets backend, not from source code."

---

## 13. Monitoring & Observability

### 📖 What to monitor in Airflow platform?

Monitoring is not only task success/failure. You also monitor scheduler and resource health.

### What to monitor
- DAG success/failure trend
- Task duration anomalies
- Scheduler delay
- Worker utilization
- Queue backlog

### Logs and Alerts
- Use task logs for first-level debugging
- Configure Email/Slack/Pager alerts for failures/SLA misses
- Use Prometheus + Grafana for platform metrics

### Example alerting strategy
1. Task failure alert: immediate Slack + email.
2. DAG SLA miss alert: warn data consumers.
3. Repeated retry alert: detect flaky upstream dependency.
4. No DAG run in expected window: scheduling health check.

### Common debugging checklist
1. Check task logs.
2. Check upstream task states.
3. Verify connection/secrets availability.
4. Check scheduler and worker health.
5. Reproduce issue with same interval parameters.

---

## 14. Cloud Integrations

### 📖 Airflow with Cloud Providers

Airflow orchestrates cloud-native services by calling provider operators/hooks.

### AWS
- S3 sensors/operators
- Redshift loads
- EMR step orchestration

**Sample flow (AWS):**
`S3KeySensor` -> `EmrAddStepsOperator` -> `EmrStepSensor` -> `Redshift load`

### Azure
- Blob storage workflows
- Synapse-oriented orchestration patterns

**Sample flow (Azure):**
Blob file arrival -> Synapse SQL transform -> publish curated table

### GCP
- GCS + BigQuery pipelines
- Dataproc orchestration

**Sample flow (GCP):**
GCS landing -> BigQuery load job -> data quality query -> publish dataset

---

## 15. Best Practices

### 📖 Production best practices checklist

1. Keep DAG files lightweight and deterministic (no heavy runtime API calls at import).
2. Keep tasks small and single-purpose.
3. Design every write path idempotent.
4. Use partition-based processing by interval.
5. Avoid large XCom payloads.
6. Use pools/queues to protect shared systems.
7. Prefer deferrable operators for long waits.
8. Configure retries, retry delay, timeout, and alerting by default.
9. Add data quality checks before final publish.
10. Version-control DAGs and validate DAG import in CI.
11. Add clear DAG docs: owner, SLA, dependency, recovery steps.
12. Track pipeline cost and duration trends.

### Example CI check
Run a DAG parse test in CI to catch broken imports before deployment.

```bash
airflow dags list
```

---

## 16. Top Review Questions (Ready Answers)

### Q1. Why use Airflow instead of cron?
**Answer:**
Cron handles time-based jobs, but Airflow adds dependency graphs, retries, task-level monitoring, backfill, UI observability, and scalable executors.

**Example:**
Cron can start one script nightly; Airflow can orchestrate 20 dependent tasks with retry and alerts.

### Q2. What is the difference between DAG, DAG Run, Task, Task Instance?
**Answer:**
DAG is definition, DAG Run is one execution for an interval, Task is a node, Task Instance is task + specific DAG Run.

### Q3. What is logical date?
**Answer:**
It is the scheduling boundary for the run's data interval, not actual runtime clock.

**Example:**
Run starts at `2026-02-23 02:00`, but logical date may be `2026-02-22` for daily interval processing.

### Q4. Why is idempotency mandatory?
**Answer:**
Because retries/backfills are normal in Airflow. Without idempotency, reruns produce duplicates or inconsistent data.

**Example:**
Use `MERGE` instead of plain append for daily incremental loads.

### Q5. Sensor vs Operator?
**Answer:**
Operator performs action; Sensor waits for condition.

### Q6. What are deferrable operators?
**Answer:**
Operators that pause on Triggerer and free worker slots during wait.

### Q7. What is XCom best used for?
**Answer:**
Small metadata passing (IDs, paths, counts), not large datasets.

### Q8. CeleryExecutor vs KubernetesExecutor?
**Answer:**
Celery: queue-based distributed workers. Kubernetes: per-task pod isolation and elastic scaling.

### Q9. How do you control Airflow concurrency?
**Answer:**
Global `parallelism`, DAG/task limits, pools, queues, and executor capacity.

### Q10. How do you handle a failed production DAG with partial load?
**Answer:**
Inspect logs/state, verify partial write impact, apply idempotent fix, rerun affected interval only, validate output.

### Q11. When should you disable catchup?
**Answer:**
Disable catchup when historical runs are not required or when back-processing old intervals can overload systems unexpectedly.

### Q12. How do you reduce worker slot wastage in sensors?
**Answer:**
Use `reschedule` mode or deferrable operators so workers are free while waiting.

### Q13. What is a pool and why use it?
**Answer:**
Pool is a concurrency guard for shared resources. Use it to cap load on fragile systems like databases/APIs.

---

## 17. One-Click Revision Sheet

### Must Remember
- Airflow = orchestrator, not compute engine.
- DAG run represents data interval.
- Logical date != actual execution timestamp.
- Idempotency enables safe retries/backfills.
- XCom is for small metadata.
- Pools protect downstream systems.
- Deferrable tasks reduce worker waste.
- Metadata DB health is critical.
- Trigger rules change downstream behavior.
- Executor choice depends on scale and infra maturity.

### High-Impact Keywords for Quick Review
- Logical date
- Data interval
- Idempotency
- Backfill
- Catchup
- Deferrable operators
- Pools and parallelism
- Metadata DB
- SLA and alerting

### 60-Second Summary Pitch
"In production, I design Airflow DAGs as thin orchestration layers. I keep tasks idempotent, use clear dependencies, and process interval-based data using logical dates. I avoid large XCom payloads, protect systems with pools and concurrency limits, and prefer deferrable sensors for long waits. For reliability, I configure retries, timeouts, and alerts, and maintain backfill-safe pipelines with strong observability through logs and metrics dashboards."
