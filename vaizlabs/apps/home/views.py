from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context, RequestContext
from django.contrib.auth.decorators import login_required
# Blog req
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
#from openshift.apps.home.models import *

##-----------------------------------------------------------------##  
## Views for home
##-----------------------------------------------------------------##  

## Index page used as main gateway
##-----------------------------------------------------------------##  
def home(request):

    return render(
        request,
        'index.html',
        {'SECTION_HOME_ACTIVE': True},
    )

## Contacts page.
##-----------------------------------------------------------------##  
def contact(request):
    return render(
        request,
        'index.html',
        {'SECTION_CONTACT_ACTIVE': True},
    )
##-----------------------------------------------------------------## 
