# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_clike'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
