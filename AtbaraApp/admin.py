from django.contrib import admin
from .models import Youtuber, Video
# Register your models here.

@admin.register(Youtuber)

class youtuber(admin.ModelAdmin):
    list_display = ['youtuber']


@admin.register(Video)

class youtuber(admin.ModelAdmin):
    list_display = ['video']