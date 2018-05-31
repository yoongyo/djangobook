from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.BookmarkLV, name="index"),
    url(r'^(?P<id>\d+)/$', views.BookmarkDV, name="detail")
]