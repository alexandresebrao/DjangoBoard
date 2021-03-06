"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from users.views.register import RegisterUser
from search.views.search import search
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^post/', include('post.urls')),
    url(r'^search/', search),
    url(r'^accounts/login/$', auth_views.login,
        {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', auth_views.logout,
        {'next_page': '/'}),
    url(r'^accounts/register/$', RegisterUser.as_view()),
    url(r'^', include('manager.urls')),
]
