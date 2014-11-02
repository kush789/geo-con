# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='fduser',
            field=models.ForeignKey(related_name=b'user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='follow',
            name='fuser',
            field=models.ForeignKey(related_name=b'following', to=settings.AUTH_USER_MODEL),
        ),
    ]
