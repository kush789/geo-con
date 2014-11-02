# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_food_language_music'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='food',
            field=models.CharField(default=b' ', max_length=b'20', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='language',
            field=models.CharField(default=b' ', max_length=b'20', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='music',
            field=models.CharField(default=b' ', max_length=b'20', blank=True),

        ),
        migrations.AlterField(
            model_name='post',
            name='placetovisit',
            field=models.CharField(default=b' ', max_length=b'20', blank=True),
        ),
    ]
