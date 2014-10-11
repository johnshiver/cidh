# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='geography',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='hours',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='jurisdiction',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
