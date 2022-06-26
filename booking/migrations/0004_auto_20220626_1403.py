# Generated by Django 3.2.13 on 2022-06-26 14:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookingName', models.CharField(blank=True, help_text='Probably the surname of your party.', max_length=100)),
                ('Guests', models.IntegerField(blank=True, default='1', help_text='Due to current government reulations this has a maximum value of 6.', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('Email', models.EmailField(help_text='Please provide email in case of cancellation.', max_length=254)),
                ('Day', models.CharField(blank=True, choices=[('Wednesday', 'WEDNESDAY'), ('Thursday', 'THURSDAY'), ('Friday', 'FRIDAY'), ('Saturday', 'SATURDAY')], max_length=9)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='barbershop',
        ),
        migrations.RemoveField(
            model_name='book',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Barbershop',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]