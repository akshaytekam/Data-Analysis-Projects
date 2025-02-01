# Spotify Data pipeline with Python, ASW, Snowflake, and Power BI

## OVERVIEW:
**The goal of this project is to build an ETL (Extract, Transform, Load) pipeline that processes and analyzes Spotify data to extract meaningful insights. The pipeline integrates Python with AWS services such as S3, Lambda, and CloudWatch, and uses SQL for data querying and analysis. The project demonstrates how to automate data workflows in a cloud-based environment.**

![solution_flow](https://github.com/user-attachments/assets/a7e173cf-d497-42ab-b4ad-f149d1795906)

## Project Architecture Flow:
**We get raw data from spotify api through cloudwatch triggers and put that data into S3 bucket, we write all logic for this using python in Lambda Function. Once the data has arrived into the S3 bucket another S3 trigger has activated automatically and data gets transformed/processed and put back into S3 bucket again. After the data transformation, this data gets transfer to the Snowflake DataWarehouse tables. Now from Snowflake tables we can use this data for various purposes like Power bi Dashboard.**

The solution uses a serverless architecture pattern with the following components:

- **Data Source:** Spotify API (Top 50 Playlist)
- **Extraction:** AWS Lambda + CloudWatch trigger (weekly)
- **Storage:** AWS S3 (Raw JSON & Transformed CSV)
- **Transformation:** AWS Lambda
- **Data Warehouse:** Snowflake
- **Data Loading:** Snowpipe/Copy command
- **Visualization:** PowerBI

### AWS S3:
- Store the raw and transformed data as JSON or CSV files.

### AWS Lambda:
- These are the functions with python code to extract the data and transform it. we can automate the pipeline using serverless functions triggered daily. Perform light data processing tasks before saving to S3.

### Environment Variables:
- It keeps our client id and secreate key secure and stored.

### Lambda Layer:
- If we want to install some external packages or library into our code, we need lambda layers to do this.

### Spotify API:
- Get the spotify developer data API with client_id and client_secrete.

### Data Model:
-- Songs Table
- song_id (PK)
- name
- duration_ms
- url
- popularity
- added_date
- album_id (FK)
- artist_id (FK)

-- Artists Table
- artist_id (PK)
- name
- url

-- Albums Table
- album_id (PK)
- name
- release_date
- total_tracks
- url

### Analytics Views:
Several analytical views were created to support business intelligence:

**Record Count Monitoring**

- Tracks total records across all entities

**Artist Analytics**

- Top 5 artists by song count in playlist
- Comprehensive artist metrics including:
  - Average popularity scores
  - Average song duration
  - Track appearances
  - Total tracks in albums

**Popularity Analysis**

- Comparison of song popularity between recent releases (last quarter) and older tracks
- Current top songs by popularity

### Business Intelligence
The PowerBI dashboard provides insights into:

![spotify dashboard pic](https://github.com/user-attachments/assets/0d124c12-fa0d-4bce-b320-8041317b7a3a)

### Tech Stack
**AWS Services**
- Lambda
- S3
- CloudWatch
- IAM

**Python Libraries**
- spotipy
- pandas
- boto3

**Data Warehouse**
- Snowflake

**BI Tool**
- PowerBI

### All Images:
**Create S3 bucket:**
![create bucket 1](https://github.com/user-attachments/assets/d4d7f504-ea28-4650-9131-0a5145c9c1ea)
![create folder inside bucket](https://github.com/user-attachments/assets/30e9db31-e032-436e-a3fe-fbd3b0c1fef5)
**Create folder inside S3:**
![fol![folder inside bucket 3](https://github.com/user-attachments/assets/77ce9f07-ce13-4f71-8f46-d0a0b5f24e82)
ders inside bucket 2](https://github.com/user-attachments/assets/7e1ed694-fba6-4864-acc1-cdd666631144)
![folder inside bucket 4](https://github.com/user-attachments/assets/6c3cc8f1-c46e-4f89-935c-0481137ece27)
**Create Lambda Data Extract Fuction:**
![create lambda function](https://github.com/user-attachments/assets/dd46dcbd-bebb-4dd6-a275-0ee62aaa7384)
**Create Environment Variable:**
![environment variable 2](https://github.com/user-attachments/assets/995b9d19-f20d-4db4-829e-55336aa8f623)
**Create Lambda Layers:**
![lambda layer 2](https://github.com/user-attachments/assets/ebb7acf2-829c-4c24-bc93-b54c2955f6d5)
**Extracted Data:**
![extracted data 1](https://github.com/user-attachments/assets/c67239e0-3350-4582-a7df-757eade5e396)

### Future Enhancements
- Add more playlist sources for broader analysis
- Implement data quality checks
- Enhance dashboard with more predictive analytics
- Add historical trend analysis
