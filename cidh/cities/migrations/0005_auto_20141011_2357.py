# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0004_auto_20141011_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='cta1_title',
            field=models.CharField(default=b'foo', max_length=256, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='cta1_url',
            field=models.CharField(default=b'foo', max_length=256, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='cta2_title',
            field=models.CharField(default=b'foo', max_length=256, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='cta2_url',
            field=models.CharField(default=b'foo', max_length=256, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='cta3_title',
            field=models.CharField(default=b'foo', max_length=256, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='cta3_url',
            field=models.CharField(default=b'foo', max_length=256, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='cta4_title',
            field=models.CharField(default=b'foo', max_length=256, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='cta4_url',
            field=models.CharField(default=b'foo', max_length=256, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='cta5_title',
            field=models.CharField(default=b'foo', max_length=256, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='cta5_url',
            field=models.CharField(default=b'foo', max_length=256, null=True, blank=True),
            preserve_default=True,
        ),
    ]
