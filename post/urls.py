from django.conf.urls import url
from post.views.create import CreateTopicView
from post.views.view import view

urlpatterns = [
    # ex: /polls/
    url(r'^(?P<forum_id>[0-9]+)/$', CreateTopicView.as_view(),
        name='createtopic'),
    url(r'^(?P<forum_id>[0-9]+)/(?P<topic_id>[0-9]+)$', view)
]
