# Generated by Django 5.0.1 on 2024-04-15 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_customer_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
    ]