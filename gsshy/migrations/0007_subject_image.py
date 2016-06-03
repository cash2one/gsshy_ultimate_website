# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsshy', '0006_auto_20160512_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='image',
            field=models.ImageField(upload_to=b'subject/%Y/%m', null=True, verbose_name='\u4e13\u9898\u56fe\u7247\u94fe\u63a5', blank=True),
        ),
    ]
