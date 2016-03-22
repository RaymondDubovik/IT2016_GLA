# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pitchify', '0008_auto_20160306_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitch',
            name='bought_stocks',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pitch',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
