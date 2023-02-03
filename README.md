# youtube_video_search

docker-compose up -> starts the django server

http://localhost:8000/videos/?ordering=-created_at -> gives a list of videos in descending order

http://localhost:8000/videos/?search=nfl  -> gives a list of videos with the keyword nfl in the ['title', 'description']

the django rest framework dashboard can be used to view all the stored videos with filtering and sorting

