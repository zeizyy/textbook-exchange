# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0006_auto_20150724_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='sold',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
