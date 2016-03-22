# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pitchify', '0007_auto_20160302_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pitch',
            name='amount_required',
        ),
        migrations.AlterField(
            model_name='pitch',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pitch',
            name='youtube_video_id',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
