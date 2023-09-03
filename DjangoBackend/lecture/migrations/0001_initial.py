# Generated by Django 4.1.10 on 2023-09-01 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('timing', models.DateTimeField()),
                ('meeting_url', models.URLField()),
            ],
        ),
    ]