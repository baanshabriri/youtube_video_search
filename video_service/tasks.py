from celery import shared_task
from video_service.serializers import Videos
from django.db import transaction
from youtube_client import youtube_keyword_search_client

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