# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_auto_20141011_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='place_purchase',
        ),
        migrations.RemoveField(
            model_name='city',
            name='place_purchase_info',
        ),
        migrations.AddField(
            model_name='city',
            name='beer',
            field=models.CharField(default=None, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='liquor',
            field=models.CharField(default=None, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='wine',
            field=models.CharField(default=None, max_length=50),
            preserve_default=True,
        ),
    ]
