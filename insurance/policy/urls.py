from django.conf.urls import include, url
from django.contrib import admin
from policy import views

app_name = 'policy'

urlpatterns = [
    url(r'Policy', views.getPolicy, name='getPolicy'),
]