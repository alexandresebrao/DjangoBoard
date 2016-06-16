from manager.models.forum import Forum
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from post.models.topic import Topic


@method_decorator(login_required, name='dispatch')
class CreateTopicView(View):
    def get(self, request, forum_id, *args, **kwargs):
        context = {}
        template = 'create.html'
        context['forum'] = Forum.objects.get(id=forum_id)
        return render(request, template, context)

    def post(self, request, forum_id, *args, **kwargs):

        topic = Topic()
        topic.user = request.user
        topic.body = request.POST['body']
        topic.title = request.POST['title']
        topic.forum = Forum.objects.get(id=forum_id)
        topic.save()
        return redirect('/forum/'+forum_id)
