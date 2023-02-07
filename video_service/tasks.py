from celery import shared_task
import requests
from video_service.serializers import VideoSerializer, Videos
from datetime import datetime, timedelta
from django.db import transaction
from youtube_client import youtube_keyword_search_client

# class Youtube_client():

#     API_KEY = 'AIzaSyALZSeqVGPD3r0aktpo0aMM0zjQY1SOTOQ'
#     BASE_URL = 'https://www.googleapis.com/youtube/v3/search'

#     def search(self, query):
#         try: 
#             publishedAfter = datetime.now() - timedelta(minutes=5)
#             params = {
#                 'part': 'snippet',
#                 'maxResults': 20,
#                 'q': query,
#                 'type': 'video',
#                 'key': self.API_KEY,
#                 'publishedAfter': publishedAfter.strftime('%Y-%m-%dT%H:%M:%SZ')
#             }
#             response = requests.get(url=self.BASE_URL, params=params)
#             if response:
#                 return response.json()
#         except Exception as e:
#             print(e)

@shared_task
def test(a,b):
    return a + b

@shared_task(name='youtube_video_getter')
def get_and_create_youtube_video_entries():
    with transaction.atomic():
        response = youtube_keyword_search_client(keyword='football')
        
        if not response or len(response) == 0:
            return None

        for video in response:
            prev_video_obj = Videos.objects.filter(video_id__exact=video['id']['videoId'])
            if prev_video_obj:
                continue
            object = Videos.objects.create(
                title=video['snippet']['title'], 
                video_id=video['id']['videoId'],
                description=video['snippet']['description'], 
                publish_date=video['snippet']['publishedAt'],
                thumbnail_meta=video['snippet']['thumbnails']
            )
            object.save()