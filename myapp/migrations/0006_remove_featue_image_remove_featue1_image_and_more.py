# Generated by Django 4.2 on 2024-10-13 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_featue_featue1_featue2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featue',
            name='image',
        ),
        migrations.RemoveField(
            model_name='featue1',
            name='image',
        ),
        migrations.RemoveField(
            model_name='featue2',
            name='image',
        ),
    ]