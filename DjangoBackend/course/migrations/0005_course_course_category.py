# Generated by Django 4.1.10 on 2023-09-04 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('course', '0004_course_course_language_course_student_enrolled'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
    ]
