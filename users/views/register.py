# coding: utf-8
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from users.models.userextension import UserExtension
from datetime import date
from django.views.generic import View
from django.contrib import messages


class RegisterUser(View):
    def get(self, request, *args, **kwargs):
        context = {}
        template = 'register.html'
        context['years'] = range(1900, date.today().year+1)
        context['months'] = range(1, 13)
        context['days'] = range(1, 32)

        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        # Checar se teve campo em branco
        user = User()
        try:
            User.objects.get(username=request.POST['username'])
            messages.info(request, "Já temos um usuário com este nome")
            return redirect('/accounts/register/')
        except:
            user.username = request.POST['username']
            user.set_password(request.POST['password'])
            if (request.POST['password'] != request.POST['v_password']):
                messages.info(request, "Senhas não batem")
                return redirect('/accounts/register/')
            birthday_day = request.POST['birthday_day']
            birthday_month = request.POST['birthday_month']
            birthday_year = request.POST['birthday_year']
            user.email = request.POST['email']
            user.save()
            us = UserExtension()
            us.user = user
            us.birthday = "%s-%s-%s" % (birthday_year, birthday_month,
                                        birthday_day)
            us.save()
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            login(request, new_user)
            return redirect('/')
