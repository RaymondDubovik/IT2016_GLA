# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pitchify', '0003_auto_20160220_0055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=1)),
                ('message', models.TextField()),
                ('answer', models.TextField()),
                ('stock_count', models.IntegerField()),
                ('price', models.IntegerField()),
                ('seen', models.BooleanField(default=False)),
                ('investor_id', models.ForeignKey(to='pitchify.Investor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pitch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('youtube_video_id', models.CharField(max_length=11)),
                ('amount_required', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('total_stocks', models.IntegerField()),
                ('price_per_stock', models.IntegerField()),
                ('company_id', models.ForeignKey(to='pitchify.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='offer',
            name='pitch_id',
            field=models.ForeignKey(to='pitchify.Pitch'),
            preserve_default=True,
        ),
    ]
