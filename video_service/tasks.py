from celery import shared_task
import requests
from video_service.serializers import VideoSerializer, Videos
from datetime import datetime, timedelta
from django.db import transaction

class Youtube_client():

    API_KEY = 'AIzaSyALZSeqVGPD3r0aktpo0aMM0zjQY1SOTOQ'
    BASE_URL = 'https://www.googleapis.com/youtube/v3/search'

    def search(self, query):
        try: 
            publishedAfter = datetime.now() - timedelta(minutes=30)
            params = {
                'part': 'snippet',
                'maxResults': 20,
                'q': query,
                'type': 'video',
                'key': self.API_KEY,
                'publishedAfter': publishedAfter.strftime('%Y-%m-%dT%H:%M:%SZ')
            }
            print(params)
            response = requests.get(url=self.BASE_URL, params=params)
            print(response)
            if response:
                return response.json()
        except Exception as e:
            print(e)

@shared_task
def test(a,b):
    return a + b

@shared_task(name='youtube_video_getter')
def get_and_create_youtube_video_entries():
    with transaction.atomic():
        client = Youtube_client()
        response = client.search(query='football')
        
        if not response:
            return
        
        responseList = response.get('items')

        if not responseList or len(responseList) == 0:
            return

        for video in responseList:
            prev_video_obj = Videos.objects.filter(video_id__exact=video['id']['videoId'])
            if prev_video_obj:
                continue
            video_object = dict(
                title=video['snippet']['title'], 
                video_id=video['id']['videoId'],
                description=video['snippet']['description'], 
                publish_date=video['snippet']['publishedAt'],
                thumbnail_meta=video['snippet']['thumbnails']
                )
            # object = VideoSerializer().create(validated_data=video_object)
            object = Videos.objects.create(
                title=video['snippet']['title'], 
                video_id=video['id']['videoId'],
                description=video['snippet']['description'], 
                publish_date=video['snippet']['publishedAt'],
                thumbnail_meta=video['snippet']['thumbnails']
            )
            object.save()