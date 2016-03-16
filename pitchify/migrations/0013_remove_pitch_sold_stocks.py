# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pitchify', '0012_auto_20160316_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pitch',
            name='sold_stocks',
        ),
    ]
