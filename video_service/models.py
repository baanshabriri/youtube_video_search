from django.db import models

class Videos(models.Model):
    id             = models.AutoField(primary_key=True)
    video_id       = models.CharField(max_length=128, unique=True, blank=False, null=False)
    title          = models.CharField(max_length=512, blank=True, null=True)
    description    = models.TextField(default=None, null=True, blank=True)
    publish_date   = models.DateTimeField(null=True, blank=True)
    thumbnail_meta = models.JSONField(default=dict, blank=True, null=True)

    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    @property 
    def get_video_details(self):
        return f'{self.title}-{self.description}'

    @property
    def get_hq_thumbnail_url(self):
        if self.thumbnail_meta.__getattribute__('high'):
            return self.thumbnail_meta.high.url

    @property
    def get_medium_thumbnail_url(self):
        if self.thumbnail_meta.__getattribute__('medium'):
            return self.thumbnail_meta.medium.url