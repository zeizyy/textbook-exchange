# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0005_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='seller',
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(null=True, to='exchange.User'),
            preserve_default=True,
        ),
    ]
