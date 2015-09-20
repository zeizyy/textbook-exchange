# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0008_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(null=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='request',
            name='author',
            field=models.CharField(null=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=300),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request',
            name='name',
            field=models.CharField(max_length=300),
            preserve_default=True,
        ),
    ]
