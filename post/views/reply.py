from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from manager.models.forum import Forum
from django.shortcuts import render


def reply(request, forum_id):
    forum = Forum.objects.get(id=forum_id)
    paginator = Paginator(forum.topic_set.all(), 25)
    context = {}
    context['forum'] = forum
    listtopic = paginator.page(1)
    context['listtopic'] = listtopic
    template = 'forum.html'
    return render(request, template, context)
