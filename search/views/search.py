from post.models.topic import Topic
from post.models.reply import Reply
from django.db.models import Q
from django.shortcuts import render


def search(request):
    search_term = request.GET['search_term']
    context = {}
    context['search_term'] = search_term
    context['topics'] = Topic.objects.filter(Q(title__icontains=search_term) |
                                             Q(body__icontains=search_term))
    context['replys'] = Reply.objects.filter(Q(body__icontains=search_term))
    template = 'results.html'
    return render(request, template, context)
