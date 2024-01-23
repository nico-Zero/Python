from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = RichTextField(default="No About...")
    avatar = models.ImageField(upload_to="avatars", default="no_picture.png")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username.capitalize()

    def like(self, post):
        if not self.is_liked(post=post):
            if self.is_disliked(post=post):
                self.un_dislike(post=post)
            like = Likes(user=self.user, post=post)
            like.save()
        else:
            self.un_like(post=post)

    def is_liked(self, post):
        try:
            self.user.likes.get(post=post)  # type: ignore
            return True
        except Exception as e:
            return False

    def un_like(self, post):
        un_like = Likes.objects.get(user=self.user, post=post)
        un_like.delete()

    def dislike(self, post):
        if not self.is_disliked(post=post):
            if self.is_liked(post=post):
                self.un_like(post=post)
            dislike = Dislikes(user=self.user, post=post)
            dislike.save()
        else:
            self.un_dislike(post=post)

    def is_disliked(self, post):
        try:
            self.user.dislikes.get(post=post)  # type: ignore
            return True
        except:
            return False

    def un_dislike(self, post):
        un_dislike = Dislikes.objects.get(user=self.user, post=post)
        un_dislike.delete()


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

    def get_like_count(self):
        likes = self.likes.all()  # type: ignore
        print(likes)


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")

    def __str__(self):
        return self.user.username + " - " + self.post.title


class Dislikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dislikes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="dislikes")

    def __str__(self):
        return self.user.username + " - " + self.post.title


class Comment(models.Model):
    comment = RichTextField(default="No Comment...")
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            "Author:- "
            + self.author.user.username.capitalize()
            + ", Blog:- "
            + self.post.title
        )
