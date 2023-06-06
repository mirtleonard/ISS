from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('logout', views.logout_user, name="logout"),
    path('login', views.login_user, name="login"),
    path('view_bugs', views.view_bugs, name="view_bugs"),
    path('register_bug', views.register_bug, name="register_bug"),
    ]