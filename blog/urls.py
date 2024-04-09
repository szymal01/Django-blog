from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from posts import views as post_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'accounts/', include('accounts.urls')),
    url(r'^posts/', include('posts.urls')),
    url(r'^about/$', views.about),
    url(r'^$', post_views.posts_list, name="home"),
    url(r'^contact', views.contact, name="contact"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)