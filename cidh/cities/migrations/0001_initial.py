# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=50)),
                ('geography', models.CharField(max_length=50)),
                ('jurisdiction', models.CharField(max_length=256)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=10)),
                ('type_of', models.CharField(max_length=50)),
                ('drink_legal', models.BooleanField(default=None)),
                ('park', models.BooleanField(default=None)),
                ('park_info', models.TextField(default=None)),
                ('street', models.BooleanField(default=None)),
                ('street_info', models.TextField(default=None)),
                ('vehicle', models.BooleanField(default=None)),
                ('vehicle_info', models.TextField(default=None)),
                ('transportation', models.BooleanField(default=None)),
                ('transportation_info', models.TextField(default=None)),
                ('place_purchase', models.CharField(max_length=50)),
                ('place_purchase_info', models.TextField(default=None)),
                ('age', models.CharField(max_length=256)),
                ('hours', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
