from django.contrib import admin
from .models import Youtuber
# Register your models here
from django.utils.html import format_html
# Register your models here.

#Admin panel customisation for Team
class YtAdmin(admin.ModelAdmin):
    #Format HTML content to render with custom title myphoto
    def myphoto(self, object):
        return format_html(f'<img src = "{object.photo.url}" width="40" />')

    list_display = ('id','name','myphoto','subs_count','is_featured') 
    search_fields = ('name', 'camera_type') 
    list_filter = ('city','camera_type') 
    list_display_links = ('id','name') 
    list_editable = ('is_featured',)

admin.site.register(Youtuber,YtAdmin)
