# IMDb Review Analytics Platform on AWS

An end-to-end cloud-native data engineering project demonstrating how to build both **batch** and **real-time** data processing pipelines on AWS using the IMDb Reviews dataset.

The platform ingests raw JSON review data into Amazon S3, transforms it into an optimized Apache Parquet dataset using AWS Glue and PySpark, performs distributed analytics with Apache Spark on Amazon EMR, and processes streaming events in real time using AWS Lambda and Amazon Kinesis.

This project was designed to showcase the core components of a modern data platform while following common data engineering practices such as ETL processing, metadata management, distributed computing, and event-driven architectures.

---

## 🚀 TL;DR

Built an end-to-end AWS data engineering platform that ingests, transforms, analyzes, and streams the IMDb Reviews dataset using AWS Glue, PySpark, Amazon Athena, Amazon EMR, AWS Lambda, and Amazon Kinesis.

- **Dataset:** IMDb Reviews (JSON)
- **Architecture:** Batch ETL + Batch Analytics + Real-Time Streaming
- **Cloud:** Amazon Web Services (AWS)
- **Languages:** Python, PySpark, SQL
- **AWS Services:** Amazon S3, AWS Glue, Amazon Athena, Amazon EMR, AWS Lambda, Amazon Kinesis
- **Output:** Partitioned Parquet datasets, SQL analytics, distributed ranking generation, and real-time suspicious activity detection

## 📂 Key Features

- End-to-end AWS data engineering platform
- Batch ETL pipeline using AWS Glue and PySpark
- JSON → Apache Parquet transformation
- Metadata management with AWS Glue Data Catalog
- SQL analytics using Amazon Athena
- Distributed Spark processing on Amazon EMR
- Event-driven architecture with AWS Lambda
- Real-time stream processing using Amazon Kinesis

---

## 📂 Architecture

The solution consists of three independent but complementary pipelines working on the same IMDb review dataset.

- **Batch ETL Pipeline** transforms raw data into an optimized analytical dataset.
- **Batch Analytics Pipeline** executes distributed Spark workloads on Amazon EMR.
- **Real-Time Streaming Pipeline** simulates live review processing using AWS serverless services.

---

### 📌 Batch ETL Pipeline

Transforms raw JSON files into partitioned Parquet datasets optimized for analytical workloads.

![Batch ETL Pipeline](architecture/batch-etl.png)

> **Goal**
>
> Transform raw IMDb review data stored in Amazon S3 into an optimized, partitioned Apache Parquet dataset that can be queried efficiently using Amazon Athena.

---

### Workflow

1. Raw JSON files are uploaded to Amazon S3.
2. AWS Glue executes a PySpark ETL job.
3. The dataset is transformed into Apache Parquet.
4. Metadata is registered in AWS Glue Data Catalog.
5. Amazon Athena queries the dataset using SQL.

---

### Why this design?

| Component | Purpose |
|-----------|---------|
| Amazon S3 | Highly scalable storage for raw and processed datasets |
| AWS Glue | Serverless ETL built on Apache Spark |
| Apache Parquet | Efficient columnar format for analytics |
| Glue Data Catalog | Centralized metadata management |
| Amazon Athena | Query data directly from S3 using SQL |

---

### Benefits

- ✅ Serverless ETL
- ✅ Reduced storage requirements
- ✅ Faster analytical queries
- ✅ Partition pruning in Athena
- ✅ Cloud-native architecture

---

### 📌 Batch Analytics Pipeline

![Batch Analytics Pipeline](architecture/batch-analytics.png)

Executes distributed Spark jobs on Amazon EMR to generate ranking results from the processed dataset.

---

### 📌 Real-Time Streaming Pipeline

![Streaming Pipeline](architecture/streaming.png)

Processes incoming review events in real time using AWS Lambda and Amazon Kinesis to detect suspicious activity.

---

## 📂 Technologies

| Category | Technologies |
|----------|--------------|
| Programming | Python, PySpark, SQL |
| Storage | Amazon S3 |
| ETL | AWS Glue |
| Metadata | AWS Glue Data Catalog |
| Query Engine | Amazon Athena |
| Distributed Computing | Amazon EMR |
| Streaming | Amazon Kinesis |
| Serverless | AWS Lambda |

---

## 📂 Batch ETL Pipeline

### 📌 Objective

Convert raw IMDb review data stored in JSON format into a partitioned Apache Parquet dataset optimized for analytical queries.

### 📌 Workflow

1. Upload raw review data to Amazon S3.
2. Read the dataset using PySpark.
3. Transform and partition the data.
4. Store the output in Apache Parquet format.
5. Register the dataset in AWS Glue Data Catalog.
6. Query the data using Amazon Athena.

*(Screenshots will be added here.)*

---

## 📂 Batch Analytics Pipeline

### 📌 Objective

Execute distributed Spark jobs on Amazon EMR to compute ranking results from the transformed IMDb dataset.

### 📌 Workflow

1. Read partitioned Parquet files from Amazon S3.
2. Launch a Spark job on Amazon EMR.
3. Perform distributed processing.
4. Store the generated ranking results back in Amazon S3.

*(Screenshots will be added here.)*

---

## 📂 Real-Time Streaming Pipeline

### 📌 Objective

Simulate a real-time review ingestion system capable of detecting suspicious activity.

### 📌 Workflow

1. Read review records from the dataset.
2. AWS Lambda publishes an event for each review.
3. Events are streamed through Amazon Kinesis.
4. A real-time processing application analyzes incoming events.
5. Suspicious events are written to a dedicated Kinesis stream.

*(Screenshots will be added here.)*

---

## 📂 Repository Structure

```text
.
├── architecture/
├── docs/
├── emr/
├── glue/
├── lambda/
├── screenshots/
├── sql/
├── streaming/
└── README.md
```

---

## 📂 Lessons Learned

Through this project I gained practical experience with:

- Building ETL pipelines using AWS Glue and PySpark
- Working with Apache Parquet and partitioned datasets
- Managing metadata with AWS Glue Data Catalog
- Querying data lakes using Amazon Athena
- Running distributed Spark workloads on Amazon EMR
- Designing event-driven architectures with AWS Lambda
- Processing streaming data using Amazon Kinesis
- Structuring cloud-native batch and streaming data pipelines

---

## 📂 Future Improvements

Possible extensions to this project include:

- Infrastructure as Code using Terraform
- Workflow orchestration with Apache Airflow or AWS Step Functions
- Automated deployment using GitHub Actions
- Data quality validation with Great Expectations
- Monitoring and alerting using Amazon CloudWatch
- Dashboarding with Amazon QuickSight
- Data lake table management with Apache Iceberg
