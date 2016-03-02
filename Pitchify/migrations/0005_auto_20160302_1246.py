# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pitchify', '0004_auto_20160302_0757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='investor_id',
            new_name='investor',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='pitch_id',
            new_name='pitch',
        ),
        migrations.RenameField(
            model_name='pitch',
            old_name='company_id',
            new_name='company',
        ),
    ]
