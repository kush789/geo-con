# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_stalk_ctr'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='food',
            field=models.TextField(default=b' ', max_length=b'20', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='language',
            field=models.TextField(default=b' ', max_length=b'20', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='music',
            field=models.TextField(default=b' ', max_length=b'20', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='placetovisit',
            field=models.TextField(default=b' ', max_length=b'20', blank=True),
            preserve_default=True,
        ),
    ]
