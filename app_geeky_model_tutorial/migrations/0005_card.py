# Generated by Django 4.0.5 on 2022-09-17 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_geeky_model_tutorial', '0004_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suit', models.IntegerField(choices=[(1, 'Diamond'), (2, 'Spade'), (3, 'Heart'), (4, 'Club')])),
            ],
        ),
    ]
