# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0013_auto_20141028_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stalk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stalked', models.ForeignKey(related_name=b'stalked', to=settings.AUTH_USER_MODEL)),
                ('stalker', models.ForeignKey(related_name=b'stalker', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
