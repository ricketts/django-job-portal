# Generated by Django 2.0 on 2019-12-01 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_joblisting_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joblisting',
            name='slug',
        ),
    ]
