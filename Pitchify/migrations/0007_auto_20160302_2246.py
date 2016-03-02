# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pitchify', '0006_auto_20160302_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='answer',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='message',
            field=models.TextField(null=True, blank=True),
        ),
    ]
