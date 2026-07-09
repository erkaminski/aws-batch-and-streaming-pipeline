CREATE EXTERNAL TABLE reviews (
  helpful array<string>,
  movie string,
  rating string,
  review_detail string,
  review_id string,
  review_summary string,
  reviewer string,
  review_date date,
  spoiler_tag bigint
)
PARTITIONED BY (
  review_year int,
  review_month int
)
STORED AS PARQUET
LOCATION 's3://612646556016-formatted-data/'
TBLPROPERTIES (
  'classification'='parquet'
);

 MSCK REPAIR TABLE `reviews`;
