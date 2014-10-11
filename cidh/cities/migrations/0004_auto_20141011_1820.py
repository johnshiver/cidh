# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_auto_20141011_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='type_of',
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]
