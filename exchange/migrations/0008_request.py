# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0007_book_sold'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('zitou', models.CharField(max_length=30)),
                ('kehao', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('professor', models.CharField(max_length=100, null=True, blank=True)),
                ('contact', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=100, null=True, blank=True)),
                ('additional', models.CharField(max_length=1000, blank=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.today)),
                ('bought', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, to='exchange.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
