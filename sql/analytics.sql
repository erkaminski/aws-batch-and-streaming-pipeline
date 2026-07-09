SELECT * FROM "student"."reviews"
limit 10;

SELECT movie, avg(cast(rating as double)) as avg_rating, regexp_extract(movie, '\(\d+\)') as movie_year
FROM "student"."reviews"
group by regexp_extract(movie, '\(\d+\)'), movie
order by movie_year desc, avg_rating desc;
