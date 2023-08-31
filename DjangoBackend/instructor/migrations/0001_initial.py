# Generated by Django 4.1.10 on 2023-08-31 09:25

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('data_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('password', models.CharField(max_length=128)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
        ),
    ]
