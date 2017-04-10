from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list')
]
#assign post_list view to ^$ url, only empty string will match
#http://127.0.0.1:8000 is not part of url in django url resolves
#views.post_list is location for above url
#name = 'post_list' sets name used to identify view, does not need to be same name