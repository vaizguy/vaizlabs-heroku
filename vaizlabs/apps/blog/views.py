# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Blog requirements
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from vaizlabs.apps.blog.models import Post
from django.template.defaulttags import register as dj_register
from imagekit import ImageSpec 
from imagekit import register as ik_register 
from imagekit.processors import ResizeToFill, TrimBorderColor, SmartResize

import logging
# Logger
logger = logging.getLogger("vaizlabs.apps.blog.view.blog")

##-----------------------------------------------------------------##  
## Views for blog
##-----------------------------------------------------------------##  

## Returns blog in following format
## * title
## * date
## * content
## * gallery
##-----------------------------------------------------------------##  
def blog(request):

    # Get all posts
    posts = Post.objects.all().order_by("-created")
    # Paginate posts in groups of 5
    paginator = Paginator(posts, 5)

    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        print 'Could not get page 1 of blog.'
        page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        print 'Received invalid or empty page.'
        posts = paginator.page(paginator.num_pages)

    return render(
        request,
        'index.html',
        dict(
            SECTION_BLOG_ACTIVE=True, 
            posts=posts, 
            user=request.user,
            ),
    )

@dj_register.simple_tag
def img_placeholder_url(post):
    return post.photos.all()[0].image.cdn_url

@dj_register.simple_tag
def img_placeholder_title(post):
    return post.photos.all()[0].title

# Imagekit thumbnail image processor
@ik_register.generator('blog:thumbnail')
class Thumbnail(ImageSpec):
    
    format = "JPEG"
    options = {"quality": 60}

    processors = [
            TrimBorderColor(),
            ResizeToFill(100, 100)
    ]

#ik_register.generator('blog:thumbnail', Thumbnail)
