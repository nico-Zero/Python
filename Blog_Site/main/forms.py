from .models import Post, Comment, Profile
from django import forms
from ckeditor.fields import RichTextField

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["about"]

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

    def save(self, commit=True, *args, **kwargs):
        instance = super(EditProfileForm, self).save(commit=False, *args, **kwargs)
        return instance.save() if commit else instance

class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, required=False)
    message = RichTextField(default="Just Want to Talk...")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "subtitle", "body", "header_image_url"]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True, *args, **kwargs):
        instance = super(PostForm, self).save(commit=False, *args, **kwargs)
        return instance.save() if commit else instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True, *args, **kwargs):
        instance = super(CommentForm, self).save(commit=False, *args, **kwargs)
        return instance.save() if commit else instance
