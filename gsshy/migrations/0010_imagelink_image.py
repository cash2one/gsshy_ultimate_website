# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsshy', '0009_auto_20160512_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagelink',
            name='image',
            field=models.ImageField(upload_to=b'imagelink/%Y/%m', null=True, verbose_name='\u56fe\u6807', blank=True),
        ),
    ]
