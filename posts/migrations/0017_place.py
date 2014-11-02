# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_auto_20141101_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('destination', models.CharField(default=b' ', max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
