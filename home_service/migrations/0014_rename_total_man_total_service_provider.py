# Generated by Django 4.2.7 on 2024-04-09 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0013_rename_service_man_service_provider'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Total_Man',
            new_name='Total_Service_Provider',
        ),
    ]
