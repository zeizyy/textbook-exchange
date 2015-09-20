# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0002_remove_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
