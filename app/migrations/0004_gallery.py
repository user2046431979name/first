# Generated by Django 4.2.5 on 2023-09-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_newsimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
