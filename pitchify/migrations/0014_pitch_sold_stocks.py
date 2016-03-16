# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pitchify', '0013_remove_pitch_sold_stocks'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitch',
            name='sold_stocks',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
