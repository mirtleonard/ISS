from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse

from bugs.service import Service


# Create your views here.

def index(request):
    print(request.user.username)
    if request.user.username != "":
        return HttpResponseRedirect('register_bug')
    return render(request, 'login.html')


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = Service.authenticate(username, password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    messages.error(request, 'Invalid username or password.')
    return HttpResponseRedirect(reverse('index'))


@login_required
def register_bug(request):
    if request.method == 'GET':
        return render(request, 'register_bug.html')
    tester = Service.get_tester(request.user.username)
    title = request.POST['title']
    description = request.POST['description']
    Service.add_bug(tester, title, description)
    return HttpResponseRedirect(reverse('view_bugs'))


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def view_bugs(request):
    bugs = Service.get_bugs()
    context = {'bugs': bugs}
    return render(request, 'view_bugs.html', context)
