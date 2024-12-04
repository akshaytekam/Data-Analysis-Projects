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

## Important Libraries:
- pip install spotipy

## Important Links:
- Spotify Docs:-  https://developer.spotify.com/documentation/web-api/tutorials/getting-started
- Get Token:- https://developer.spotify.com/dashboard/71a5129d70d142279bf08eac17a8ed77/settings

## AWS Services Flow And Architechture
- First created the AWS S3 bucket with name (spotify-etl-project-akki)
- Create below folder architechture:
    - raw_data
        - processed (already processed)
        - to_processed (yet to process)
    - transformed_data
        - album_data
        - songs_data
        - artist_data
- Open Lambda service and create a function name (spotify_api_data_extract)
- Next add environment variable for our client_id and client_secret
- Inside Lambda service create a new layer as well for importing spotify packages and use it in AWS environment. Upload the given (spotipy_layer.zip) file.
- In this function implement boto3 library to interact with AWS services. So using this we dump our entire json data into S3.
- Next create a IAM role here so that any two servicess in AWS can talk to each other by providing them full S3 permissions.
- After deploying and running this function, we'll get a json file extracted like below:
![s1](https://github.com/user-attachments/assets/6a71fc61-05d1-4d66-a071-f11d9c15d064)

- Now create another function for transformation of raw data with name (spotify_transformation_load_function)
- WE can use the same IAM role for this function as well.
- Here we have to do two things now:
    - take the data from folder to_processed and transform it completly and put it into transformed_data folder respectively.
    - Once the data is processed we need to move that data from to_processed folder into processed folder. So that we don't process the same data again.
- Once everything done, add the triggers from AWS CloudWatch to automate the process.
- Now use the AWS Glue Crawler to get the schema information and put it in a table format.
- And at last use Athena to run the SQL queries to view the data and do analysis with this entire pipeline.

![athena](https://github.com/user-attachments/assets/0def5a73-a833-4e90-a842-9ffdc1d13853)



