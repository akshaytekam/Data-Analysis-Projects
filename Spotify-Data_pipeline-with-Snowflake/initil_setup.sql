create or replace database MANAGE_DB;
create or replace schema EXTERNAL_STAGES;

create or replace database spotify_db;
create or replace schema spotify_top_50;

-- storage integration connection created in private for security reasons.
-- storage integration name created: s3_init_spotify_bucket

create or replace stage manage_db.external_stages.spotify_s3_bucket
url = 's3://spotify-etl-pipeline-akki/transformed_data/'
storage_integration = s3_init_spotify_bucket
file_format = MANAGE_DB.FILE_FORMATS.CSV_FILE;

CREATE OR REPLACE FILE FORMAT MANAGE_DB.FILE_FORMATS.CSV_FILE
TYPE = 'CSV'
FIELD_DELIMITER = ','             
SKIP_HEADER = 1                   
FIELD_OPTIONALLY_ENCLOSED_BY = '"' ;

-- Create all three tables

create or replace table SPOTIFY_DB.SPOTIFY_TOP_50.ALBUMS(
    album_id string,
    album_name string,
    release_date date,
    total_tracks int,
    album_url string
);


create or replace table SPOTIFY_DB.SPOTIFY_TOP_50.ARTISTS(
    artist_id string,
    artist_name string,
    artist_url string
);

create or replace table SPOTIFY_DB.SPOTIFY_TOP_50.SONGS(
    song_id string,
    song_name string,
    song_duration_ms int,
    song_url string,
    popularity int,
    added_date date,
    album_id string,
    artist_id string
);

-- testing connection
list @MANAGE_DB.EXTERNAL_STAGES.SPOTIFY_S3_BUCKET;

DESC INTEGRATION s3_init_spotify_bucket;


copy into SPOTIFY_DB.SPOTIFY_TOP_50.ALBUMS
from @MANAGE_DB.EXTERNAL_STAGES.SPOTIFY_S3_BUCKET
file_format = (FORMAT_NAME = MANAGE_DB.FILE_FORMATS.CSV_FILE)
pattern = 'transformed_data/album_data/.*'
force = true;

copy into SPOTIFY_DB.SPOTIFY_TOP_50.ARTISTS
from @MANAGE_DB.EXTERNAL_STAGES.SPOTIFY_S3_BUCKET
pattern = 'transformed_data/artist_data/.*'
force = true;

copy into SPOTIFY_DB.SPOTIFY_TOP_50.SONGS
from @MANAGE_DB.EXTERNAL_STAGES.SPOTIFY_S3_BUCKET
pattern = 'transformed_data/songs_data/.*'
force = true;

SELECT * FROM SPOTIFY_DB.SPOTIFY_TOP_50.ALBUMS LIMIT 10;
SELECT * FROM SPOTIFY_DB.SPOTIFY_TOP_50.ARTISTS LIMIT 10;
SELECT * FROM SPOTIFY_DB.SPOTIFY_TOP_50.SONGS LIMIT 10;

select count(*) from albums;
truncate albums;
truncate songs;
truncate artists;

desc stage MANAGE_DB.EXTERNAL_STAGES.SPOTIFY_S3_BUCKET;
