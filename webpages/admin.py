from django.contrib import admin
from webpages.models import Slider, Team
# Register your models here.

#Admin panel customisation for Team
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','role','created_date') #to show the fields
    list_display_links = ('first_name','id') #to make the first_name, id clickable
    search_fields = ('first_name', 'role') #search field options
    list_filter = ('role',) #filter options by role

admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)