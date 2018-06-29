
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'forum'

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'post_message/', views.post_message, name='post_message'),
]
