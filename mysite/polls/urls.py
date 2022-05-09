from django.conf.urls.defaults import url

from . import views

urlpatterns = (
    url(r'^$', views.index),
    url(r'^vote/(?P<choice_id>\d+)$', views.vote),
)
