# Generated by Django 5.0.2 on 2024-04-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0004_alter_userprofile_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
    ]
