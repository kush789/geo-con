# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_placetovisit'),
    ]

    operations = [
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('food', models.CharField(default=b' ', max_length=b'30')),
                ('destination', models.ForeignKey(to='posts.place')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(default=b' ', max_length=b'30')),
                ('destination', models.ForeignKey(to='posts.place')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='music',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('music', models.CharField(default=b' ', max_length=b'30')),
                ('destination', models.ForeignKey(to='posts.place')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
