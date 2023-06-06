from django.contrib.auth import authenticate
from django.utils import timezone
from bugs.models import *


class Service:
    @staticmethod
    def add_bug(tester, title, description):
        bug = Bug(tester=tester, title=title, description=description, date_reported=timezone.now())
        bug.save()

    @staticmethod
    def get_bugs():
        bugs = Bug.objects.all()
        return bugs

    @staticmethod
    def get_tester(username):
        return Tester.objects.get(username=username)

    @staticmethod
    def authenticate(username, password):
        return authenticate(username=username, password=password)