from django.db import models
from datetime import datetime

# Create your models here.
class Youtuber(models.Model):
    crew_choices = (
        ('solo','solo'),
        ('small','small'),
        ('large','large'),
    )

    camera_choices = (
        ('canon','canon'),
        ('nikon','nikon'),
        ('sony','sony'),
        ('red','red'),
        ('fuji','fuji'),
        ('panasonic','panasonic'),
        ('other','other'),
    )

    category_choices = (
            ('code','code'),
            ('mobile_review','mobile_review'),
            ('vlogs','vlogs'),
            ('comedy','comedy'),
            ('gaming','gaming'),
            ('film_making','film_making'),
            ('cooking','cooking'),
        )

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to = 'media/ytubers/%Y/%m/')
    video_url = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(max_length=255, choices=crew_choices)
    camera_type = models.CharField(max_length=255,choices=camera_choices)
    subs_count = models.CharField(max_length=255)
    category = models.CharField(max_length=255,choices=category_choices)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now,blank=True)