# Generated by Django 4.2 on 2023-04-21 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_post_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
