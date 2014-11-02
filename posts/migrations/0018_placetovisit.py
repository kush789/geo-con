# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='placetovisit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.CharField(default=b' ', max_length=b'30')),
                ('destination', models.ForeignKey(to='posts.place')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
