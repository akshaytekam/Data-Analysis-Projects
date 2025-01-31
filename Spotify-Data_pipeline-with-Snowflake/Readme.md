# Spotify Data pipeline with Python, ASW, Snowflake, and Power BI

## OVERVIEW:
**The goal of this project is to build an ETL (Extract, Transform, Load) pipeline that processes and analyzes Spotify data to extract meaningful insights. The pipeline integrates Python with AWS services such as S3, Lambda, and CloudWatch, and uses SQL for data querying and analysis. The project demonstrates how to automate data workflows in a cloud-based environment.**

### AWS S3:
- Store the raw and transformed data as JSON or CSV files.

### AWS Lambda:
- Automate the pipeline using serverless functions triggered daily. Perform light data processing tasks before saving to S3.

### Environment Variables:
- It keeps our client id and secreate key secure and stored.

### Lambda Layer:
- If we want to install some external packages or library into our code, we need lambda layers to do this.
