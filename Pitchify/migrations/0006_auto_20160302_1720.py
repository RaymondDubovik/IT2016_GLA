# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pitchify', '0005_auto_20160302_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.CharField(default=b'P', max_length=1, choices=[(b'P', b'Pending'), (b'A', b'Accepted'), (b'D', b'Declined')]),
        ),
        migrations.AlterField(
            model_name='pitch',
            name='youtube_video_id',
            field=models.CharField(max_length=11, null=True, blank=True),
        ),
    ]
