from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.posts_list, name="list"),
    url(r'^search', views.search, name="search"),
    url(r'^create/$', views.post_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/update', views.post_update, name="update"),
    url(r'^(?P<slug>[\w-]+)/delete', views.post_delete, name="delete"),
    url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name="detail"),
    url(r'^comment', views.comment_create, name="comment"),
]
