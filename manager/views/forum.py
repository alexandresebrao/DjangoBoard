from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from manager.models.forum import Forum
from django.shortcuts import render


def forum(request, forum_id):
    forum = Forum.objects.get(id=forum_id)
    topics = forum.topic_set.all()
    paginator = Paginator(topics, 25)  # Show 25 contacts per page
    context = {}
    context['forum'] = forum
    try:
        listtopic = paginator.page(0)
    except:
        listtopic = None
    context['listtopic'] = listtopic
    template = 'forum.html'
    return render(request, template, context)


def page(request, forum_id, page_id):
    forum = Forum.objects.get(id=forum_id)
    topics = forum.topic_set.all()
    paginator = Paginator(topics, 25)  # Show 25 contacts per page
    context = {}
    context['forum'] = forum
    try:
        listtopic = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        listtopic = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        listtopic = paginator.page(paginator.num_pages)

    context['listtopic'] = listtopic
    template = 'forum.html'
    return render(request, template, context)
