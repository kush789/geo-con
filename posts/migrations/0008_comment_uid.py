# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_comment_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='uid',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
