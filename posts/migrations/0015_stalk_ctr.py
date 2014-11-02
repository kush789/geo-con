# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_stalk'),
    ]

    operations = [
        migrations.AddField(
            model_name='stalk',
            name='ctr',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
