# youtube_video_search

docker-compose up -> starts the django server, redis, celery, celery-beat and postgres db

docker-compose up -d -> starts the django server, redis, celery, celery-beat and postgres db in the background

http://localhost:8000/videos/?ordering=-created_at -> gives a list of videos in descending order

http://localhost:8000/videos/?search=nfl  -> gives a list of videos with the keyword nfl in the ['title', 'description']

the django rest framework dashboard can be used to view all the stored videos with filtering and sorting


Notes: have committed the .env.dev for ease of use along with api key for the youtube app which should not be stored in a public configuration.
