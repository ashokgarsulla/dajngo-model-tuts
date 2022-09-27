from django.contrib import admin
from app_geeky_model_tutorial.models import (
    StudentModel,
    Person,
    Student,
    Card,
    MyUUIDModel,
    FieldTypeModel,
    Blog,
    Author,
    Entry,
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

@admin.register(FieldTypeModel)
class FieldTypeModelAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in FieldTypeModel._meta.fields]

@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Author._meta.fields]

@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Blog._meta.fields]

@admin.register(Entry)
class EntryModelAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Entry._meta.fields]