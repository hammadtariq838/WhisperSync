# Generated by Django 4.2.2 on 2023-07-06 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subtitles', '0002_subtitle_is_charged'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtitle',
            old_name='is_charged',
            new_name='is_paid',
        ),
    ]
