# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pitchify', '0011_auto_20160311_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.CharField(default=b'?', max_length=1, choices=[(b'?', b'Pending'), (b'A', b'Accepted'), (b'D', b'Declined')]),
        ),
        migrations.AlterField(
            model_name='offer',
            name='stock_count',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='pitch',
            name='price_per_stock',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='pitch',
            name='total_stocks',
            field=models.PositiveIntegerField(),
        ),
    ]
