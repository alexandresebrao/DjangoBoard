from post.models.topic import Topic
from post.models.reply import Reply
from django.db.models import Q
from django.shortcuts import render


def find_user_by_name(request, serch_term):
    context = {}
    context['topic'] = Topic.objects.filter(Q(title__icontains=serch_term) |
                                            Q(body__icontains=serch_term))
    context['topic'] = Reply.objects.filter(Q(body__icontains=serch_term))
    template = 'result.html'
    return render(request, template, context)
