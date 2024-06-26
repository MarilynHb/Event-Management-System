# Generated by Django 5.0.2 on 2024-04-06 11:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0006_filelink'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportEvent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reported_on', models.DateTimeField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='event_management.event')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='report_event', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
