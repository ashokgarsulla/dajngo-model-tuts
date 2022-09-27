import uuid
from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class StudentModel(models.Model):
    stid = models.IntegerField()
    sname = models.CharField(max_length=50)
    semail = models.EmailField(max_length=50)
    spass = models.CharField(max_length=90)
    comment = models.CharField(max_length=100, default="Not Available")

    def __str__(self):
        return self.sname

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZES)

    def __str__(self):
        return self.name


class Student(models.Model):

    class YearInSchool(models.TextChoices):
        FRESHMAN = 'FR', _('Freshman')
        SOPHOMORE = 'SO', _('Sophomore')
        JUNIOR = 'JR', _('Junior')
        SENIOR = 'SR', _('Senior')
        GRADUATE = 'GR', _('Graduate')

    year_in_school = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {
            self.YearInSchool.JUNIOR,
            self.YearInSchool.SENIOR,
        }

class Card(models.Model):

    class Suit(models.IntegerChoices):
        DIAMOND = 1
        SPADE = 2
        HEART = 3
        CLUB = 4

    suit = models.IntegerField(choices=Suit.choices)

class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class FieldTypeModel(models.Model):
    auto_field_example = models.AutoField(primary_key=True)
    boolean_field_exaple = models.BooleanField()
    char_field_example = models.CharField( max_length=50)
    date_field_exmaple = models.DateField()
    datetme_field_example = models.DateTimeField(auto_now=False, auto_now_add=False)
    decimal_example =models.DecimalField(max_digits=5, decimal_places=2)
    duration_exaple = models.DurationField()
    email_example = models.EmailField(max_length=254)
    file_example = models.FileField(upload_to="fieldexample", max_length=100)
    # file_path_example = models.FilePathField(path='', match=None, recursive=False, allow_files=True, allow_folders=False, max_length=100)
    float_example = models.FloatField()
    ip_exaple = models.FloatField()
    imagne_exmaple =models.ImageField(upload_to="modelimage", height_field=None, width_field=None, max_length=None)
    integer_example = models.IntegerField()
    json_example = models.JSONField (encoder=None, decoder=None)
    slug_example = models.SlugField()
    small_integer_exaple = models.SmallIntegerField()
    txtfield_example = models.TextField()
    time_exaple = models.TimeField( auto_now=False, auto_now_add=False)
    url_example = models.URLField(max_length=200)
    uuid_eaxmple = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    # relation_with_my_uuid_cascade = models.ForeignKey(MyUUIDModel,on_delete=models.CASCADE)
    # relation_with_my_uuid_protect = models.ForeignKey(Card,on_delete=models.PROTECT)
    # relation_with_my_uuid_restrict = models.ForeignKey(Student,on_delete=models.RESTRICT)
    def __str__(self):
        return self.char_field_example


# //////////////////////////////////////////////////////////////////////////////////////////////////////
#                      BELOW TABLE IS CREATING FOR QUERY PURPOSE
# //////////////////////////////////////////////////////////////////////////////////////////////////////

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline