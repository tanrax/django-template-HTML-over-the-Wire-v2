# Generated by Django 4.1.1 on 2022-12-17 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_cat_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='channel',
            new_name='channel_name',
        ),
    ]
