# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20141025_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.FileField(null=True, upload_to=posts.models.get_upload_file_name, blank=True),
            preserve_default=True,
        ),
    ]
