from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

LANG_CHOICES = [
    ('lang_1', 'lang_1'),
    ('lang_1', 'lang_2')
]

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANG_CHOICES)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField( default=datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    public = models.BooleanField(default=True)

class Comment(models.Model):
   text = models.TextField(max_length=1000)
   creation_date = models.DateTimeField( default=datetime.now())
   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
   snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE, related_name='comments')