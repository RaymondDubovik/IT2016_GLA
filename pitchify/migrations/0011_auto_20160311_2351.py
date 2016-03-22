# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pitchify', '0010_auto_20160311_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitch',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pitch',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
