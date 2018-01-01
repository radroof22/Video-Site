from django.contrib import admin

# Register your models here.

from .models import Video, Article

admin.site.register(Video)
admin.site.register(Article)

