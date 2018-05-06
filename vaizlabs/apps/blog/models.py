# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

from pyuploadcare.dj.models import ImageField

class PostPhoto(models.Model):
    id = models.AutoField(primary_key=True)    
    title = models.CharField(max_length=200)
#    image     = ProcessedImageField(
#            upload_to="blog/post_pics", 
#            null=False, 
#            blank=False, 
#            processors=[ResizeToFit(800, 450)],
#            format = "JPEG",
#            options = {"quality": 80},
#            )
    # Uploadcare image field
    image = ImageField(blank=True, manual_crop="")
    timestamp = models.DateTimeField(
            auto_now_add=True, 
            auto_now=False,
            )
    post_id   = models.ForeignKey(
            "Post", 
            on_delete=models.CASCADE,
            related_name="photos",
            )

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp"]
    
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title    = models.CharField(max_length=60)
    content  = models.TextField()
    created  = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_id  = models.ForeignKey(
            User,
            related_name="userblogpost",
            blank=True,
            null=True,
            verbose_name=u"User ID",
            )
    PostPhoto = None

    def __unicode__(self):
        return self.title

    def __meta__(self):
        ordering = ("created")
        get_latest_by = ("created")
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

