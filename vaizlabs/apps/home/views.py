from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context, RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
# Blog req
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
#from openshift.apps.home.models import *

##-----------------------------------------------------------------##  
## Views for vaizlabs
##-----------------------------------------------------------------##  

## Index page. Main gateway for vaizlabs
##-----------------------------------------------------------------##  
def home(request):

    return render_to_response(
        'index.html',
        {'SECTION_HOME_ACTIVE': True},
        RequestContext(request)
    )

## Blog
##-----------------------------------------------------------------##  
def blog(request):

    #posts = Post.objects.all().order_by("-created")
    posts = []
    #paginator = Paginator(posts, 5)

    #try:
    #    page = int(request.GET.get("page", '1'))
    #except ValueError:
    #    print 'Could not get page 1 of blog.'
    #    page = 1

    #try:
    #    posts = paginator.page(page)
    #except (InvalidPage, EmptyPage):
    #    print 'Received invalid or empty page.'
    #    posts = paginator.page(paginator.num_pages)

    return render_to_response(
        'index.html',
        #dict(SECTION_BLOG_ACTIVE=True, posts=posts, user=request.user),
        dict(SECTION_BLOG_ACTIVE=True, posts=posts, user=request.user),
        RequestContext(request)
    )

## Contacts page.
##-----------------------------------------------------------------##  
def contact(request):
    return render_to_response(
        'index.html',
        {'SECTION_CONTACT_ACTIVE': True},
        RequestContext(request)
    )
##-----------------------------------------------------------------## 
