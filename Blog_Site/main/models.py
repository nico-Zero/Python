from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = RichTextField(default="No About...")
    avatar = models.ImageField(upload_to="avatars", default="no_picture.png")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username.capitalize()


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=1000, blank=False)
    subtitle = models.CharField(max_length=1000, blank=True)
    body = RichTextField(default="No Body...")
    header_image_url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title.capitalize()


class Comment(models.Model):
    comment = RichTextField(default="No Comment...")
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Author:- " + self.author.user.username.capitalize() + ", Post:- " + self.post.title
