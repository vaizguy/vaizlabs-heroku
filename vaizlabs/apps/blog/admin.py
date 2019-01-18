# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from vaizlabs.apps.blog.models import Post, PostPhoto

class PostPhotoInline(admin.TabularInline):
    model = PostPhoto
    fields = ["image"]
    max_num = 10


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ["title", "created", "modified", "user_id"]
    inlines = [PostPhotoInline,]
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)
