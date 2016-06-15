from manager.models.category import Category
from django.shortcuts import render


def index(request):
    context = {}
    category = Category.objects.all()
    context['category'] = category
    template = 'index.html'
    return render(request, template, context)
