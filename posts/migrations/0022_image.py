# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0021_auto_20141101_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.FileField(null=True, upload_to=b'')),
                ('destination', models.ForeignKey(to='posts.place')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
