# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0013_auto_20150802_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='request',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
