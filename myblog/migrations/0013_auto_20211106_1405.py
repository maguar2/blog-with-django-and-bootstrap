# Generated by Django 3.2.7 on 2021-11-06 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0012_auto_20211106_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='full_path',
            field=models.TextField(default='myblog/'),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_description',
            field=models.CharField(default='new', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_keywords',
            field=models.CharField(default='new', max_length=255),
        ),
    ]