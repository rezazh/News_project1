# Generated by Django 4.2 on 2023-04-24 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_postlike_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='postlike',
            unique_together=set(),
        ),
    ]
