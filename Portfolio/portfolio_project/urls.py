"""portfolio_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from port_main import views as pm_views
from AngryDice import views as angry_views
from JavaPic import views as javapic_views
from RandomQuote import views as random_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', pm_views.home_page),
    url(r'^AngryDice$', angry_views.AngryDice, name="AngryDice"),
    url(r'^JavaPic$', javapic_views.index, name="index"),
    url(r'^Gallery$', javapic_views.gallery, name="gallery"),
    url(r'^Join$', javapic_views.join, name="join"),
    url(r'^RandomQuote$', random_views.RandomQuote, name="RandomQuote"),
]
