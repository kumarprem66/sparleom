# Generated by Django 4.1.10 on 2023-09-03 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_course_price_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='rating_count',
            field=models.IntegerField(default=20),
        ),
    ]
