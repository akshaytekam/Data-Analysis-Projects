CREATE or replace STORAGE INTEGRATION s3_init_spotify_bucket
    TYPE = EXTERNAL_STAGE
    STORAGE_PROVIDER = S3
    ENABLED = TRUE
    STORAGE_AWS_ROLE_ARN = ''
    STORAGE_ALLOWED_LOCATIONS = ('s3://spotify-etl-pipeline-akki')
     COMMENT = 'Creating connection to s3'

DESCRIBE STORAGE INTEGRATION s3_init_spotify_bucket;
