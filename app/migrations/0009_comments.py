# Generated by Django 4.2.5 on 2023-10-02 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_news_options_alter_newsimages_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('newsObject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.news')),
            ],
        ),
    ]
