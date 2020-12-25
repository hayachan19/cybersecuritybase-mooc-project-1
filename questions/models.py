from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Question(models.Model):
    assignee = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=None
    )
    title = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    content = models.TextField(
        blank=True,
        default=''
    )
    def __str__(self):
        return self.title
