# Generated by Django 4.1.10 on 2023-09-01 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='date',
        ),
    ]
