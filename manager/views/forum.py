from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from manager.models.forum import Forum
from django.shortcuts import render


def forum(request, forum_id):
    forum = Forum.objects.get(id=forum_id)
    paginator = Paginator(forum.topic_set.all(), 25)
    context = {}
    context['forum'] = forum
    listtopic = paginator.page(1)
    context['listtopic'] = listtopic
    template = 'forum.html'
    return render(request, template, context)


def page(request, forum_id, page_id):
    forum = Forum.objects.get(id=forum_id)
    paginator = Paginator(forum.topic_set.all(), 25)
    context = {}
    context['forum'] = forum
    try:
        listtopic = paginator.page(page_id)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        listtopic = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        listtopic = paginator.page(paginator.num_pages)

    context['listtopic'] = listtopic
    template = 'forum.html'
    return render(request, template, context)
