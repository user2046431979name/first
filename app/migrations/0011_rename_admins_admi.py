# Generated by Django 4.2.5 on 2023-10-07 12:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_admins'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admins',
            new_name='Admi',
        ),
    ]