from post.models.topic import Topic
from manager.models.forum import Forum
from django.shortcuts import render


def view(request, forum_id, topic_id):
    context = {}
    forum = Forum.objects.get(id=forum_id)
    context['forum'] = forum
    topic = Topic.objects.get(id=topic_id)
    context['topic'] = topic
    template = 'view.html'
    return render(request, template, context)
