# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0011_user_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='contact',
        ),
    ]
