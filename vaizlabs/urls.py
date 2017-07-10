"""vaizlabs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from vaizlabs.apps.home.views import home, blog, contact

urlpatterns = [
    # Home
    url(r'^$', home, name='home'),
    url(r'^home$', home, name='home'),
      
    # Blog 
    url(r'^blog', blog, name='blog'),

    # Contact 
    url(r'^contact$', contact, name='contact'),

    url(r'^admin/', include(admin.site.urls)),
]
