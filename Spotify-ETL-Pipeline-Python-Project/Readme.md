# Spotify ETL Pipeline Python Project

## Overview:
**The goal of this project is to build an ETL (Extract, Transform, Load) pipeline that processes and analyzes Spotify data to extract meaningful insights. 
The pipeline integrates Python with AWS services such as S3, Lambda, and CloudWatch, and uses SQL for data querying and analysis. 
The project demonstrates how to automate data workflows in a cloud-based environment.**

## ETL Process
![etl process](https://github.com/user-attachments/assets/353aa24e-cb47-4380-bd60-4a1f918f48b5)

## Project Architecture
![Project Artichecture](https://github.com/user-attachments/assets/402870b0-e582-4494-9bd8-3615e3ca396e)

## Spotify API
![api](https://github.com/user-attachments/assets/e845d3a1-9ac2-48c7-8ca6-a61e01fe5a8b)

## Tools and Technologies Used

### Python:
- Extract data from Spotify API using requests or spotipy.
Perform data transformation using pandas or native Python functions.

### AWS S3:
- Store the raw and transformed data as JSON or CSV files.

### AWS Lambda:
- Automate the pipeline using serverless functions triggered daily.
Perform light data processing tasks before saving to S3.

### AWS Glue:
- Crawl S3 buckets to catalog data.
Use Glue ETL scripts for additional transformation.

### AWS Athena:
- Run SQL queries on the cataloged data for insights and analytics.

### AWS CloudWatch:
- Monitor and log pipeline performance.
Schedule daily triggers for Lambda functions.

## Pipeline Workflow

### Extraction:
- Use Spotify's API to fetch data on songs, artists, and playlists.
Save raw JSON files to an S3 bucket.

### Transformation:
- Clean, filter, and normalize the data in Python or AWS Glue.
Convert raw data into structured formats like CSV or Parquet.

### Loading:
- Store the processed data in another S3 bucket or table.

### Analysis:
- Use AWS Athena to query the processed data.
Enable stakeholders to generate insights or create dashboards using tools like Tableau or Power BI.

## Benefits and Use Cases
- Gain insights into Spotify trends and music patterns.
- Build recommendations or visualizations based on the data.
- Demonstrate expertise in ETL pipelines, cloud computing, and data analysis.
