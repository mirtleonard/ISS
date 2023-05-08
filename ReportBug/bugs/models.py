from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tester(User):
    def __str__(self):
        return self.username


class Developer(User):
    def __str__(self):
        return self.username


class Bug(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_reported = models.DateTimeField('date reported')
    date_resolved = models.DateTimeField('date resolved', null=True, blank=True)
    resolved = models.BooleanField(default=False)
    creator = models.ForeignKey(Tester, on_delete=models.CASCADE, related_name='creator')

    def __str__(self):
        return self.title

