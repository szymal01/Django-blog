from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    draft = models.BooleanField(default=False)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+'...'

class Comment(models.Model):
    post = models.ForeignKey(Post, default=None, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(sefl):
        return sefl.body
