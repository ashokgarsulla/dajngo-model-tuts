from django.contrib import admin
from .models import Person,Musician,Album
# Register your models using decoratorhere.
# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#  list_display = ['id', 'first_name', 'last_name']


admin.site.register(Person)



#  to display more than one field in admin interface
# create model 
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','instrument')
admin.site.register(Musician,MusicianAdmin)
admin.site.register(Album)
