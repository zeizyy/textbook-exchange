# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('zitou', models.CharField(max_length=30)),
                ('kehao', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('professor', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField()),
                ('seller', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=100)),
                ('new', models.CharField(max_length=30)),
                ('additional', models.CharField(blank=True, max_length=1000)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.today)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
