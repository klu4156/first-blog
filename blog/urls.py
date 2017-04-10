from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
#assign post_list view to ^$ url, only empty string will match
#http://127.0.0.1:8000 is not part of url in django url resolves
#views.post_list is location for above url
#name = 'post_list' sets name used to identify view, does not need to be same name

#second: post/ - first word after beginning is post
#middle part passes pk to views as a variable
#d+ means at least one digit
#/$ means slash and end of url