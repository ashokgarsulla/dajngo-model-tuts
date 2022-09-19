from django.contrib import admin
from app_geeky_model_tutorial.models import (
    StudentModel,
    Person,
    Student,
    Card,
    MyUUIDModel,
    )

# admin.site.register(StudentModel)

# register using decorator
@admin.register(StudentModel)
class SdudentModelAdnin(admin.ModelAdmin):
    list_display = ('id','stid','sname','semail','spass','comment')

# admin.site.register(StudentModel,SdudentModelAdnin)

@admin.register(Person)
class PersonAdnin(admin.ModelAdmin):
    list_display = ('id','name','shirt_size')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','year_in_school')

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id','suit')

@admin.register(MyUUIDModel)
class MyUUIDModelAdmin(admin.ModelAdmin):
    list_display = ('id','name')