from django.conf.urls import url
from post.views.create import CreateTopicView


urlpatterns = [
    # ex: /polls/
    url(r'^(?P<forum_id>[0-9]+)/$', CreateTopicView.as_view(),
        name='createtopic'),
]
