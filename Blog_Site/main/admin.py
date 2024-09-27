from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.Likes)
admin.site.register(models.Dislikes)
