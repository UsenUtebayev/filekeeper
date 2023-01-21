from django.contrib import admin

from videokeeper.models import VideoModel


# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(VideoModel, VideoAdmin)
