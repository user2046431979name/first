# Generated by Django 4.2.5 on 2023-09-26 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('news_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.news')),
            ],
        ),
    ]
