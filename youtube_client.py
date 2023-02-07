# https://developers.google.com/explorer-help/code-samples#python

import os
from datetime import datetime, timedelta
import googleapiclient.discovery


def youtube_keyword_search_client(keyword):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = 'youtube'
    api_version      = 'v3'
    DEVELOPER_KEY    = os.environ.get('YOUTUBE_API_KEY', 'AIzaSyAHgrJ5okyiKBrh6NlYoQsUfkfM3mzNYfA')

    response_list    = []
    try:
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = DEVELOPER_KEY)

        published_after = datetime.now() - timedelta(minutes=5)
        request = youtube.search().list(
            part='snippet',
            maxResults=25,
            q=keyword,
            type='video',
            publishedAfter=published_after.strftime('%Y-%m-%dT%H:%M:%SZ')
        )
        response = request.execute()
        response_list = dict(response).get('items', [])
        next_page_token = dict(response).get('nextPageToken', None)
        while next_page_token is not None:
            request = youtube.search().list(
                part='snippet',
                maxResults=25,
                q='football',
                type='video',
                pageToken=next_page_token,
                publishedAfter=published_after.strftime('%Y-%m-%dT%H:%M:%SZ')
            )
            response = request.execute()
            response_list = [*response_list, *dict(response).get('items', [])]
            next_page_token = dict(response).get('nextPageToken', None)
    except Exception as e:
        print(e)

    return response_list
