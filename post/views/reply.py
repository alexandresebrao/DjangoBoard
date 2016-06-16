from post.models.reply import Reply
from post.models.topic import Topic
from django.shortcuts import redirect


def reply(request, topic_id):
    reply = Reply()
    reply.body = request.POST['body']
    reply.user = request.user
    reply.topic = Topic.objects.get(id=topic_id)
    reply.save()
    string_redirect = "/post/%s/%s" % (reply.topic.forum.id, reply.topic.id)
    return redirect(string_redirect)
