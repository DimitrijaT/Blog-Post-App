# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class BlogUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="photos/", null=True, blank=True)
    interests = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    profession = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    content = models.TextField()
    # auto_now_add is added automatically when creating a post
    creation_date = models.DateTimeField(auto_now_add=True)
    # auto_now is added automatically when editing a post
    last_modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class File(models.Model):
    file = models.FileField(upload_to="files/", null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name


class Block(models.Model):
    blocker = models.ForeignKey(BlogUser, on_delete=models.CASCADE, related_name="user_blocker")
    blocked = models.ForeignKey(BlogUser, on_delete=models.CASCADE, related_name="user_blocked")

    def __str__(self):
        return str(self.blocker) + " blocked " + str(self.blocked)
