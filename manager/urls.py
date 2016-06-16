from django.conf.urls import url
from manager.views.forum import forum
from manager.views.forum import page
from manager.views.about import AboutView
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^forum/(?P<forum_id>[0-9]+)/$', forum,
        name='forum'),
    url(r'^forum/(?P<forum_id>[0-9]+)/(?P<page_id>[0-9]+)$', page,
        name='page'),
    url(r'^about/', AboutView.as_view()),
]
