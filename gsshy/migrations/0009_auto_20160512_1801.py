# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsshy', '0008_auto_20160512_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='download_file4',
        ),
        migrations.RemoveField(
            model_name='article',
            name='download_file5',
        ),
        migrations.RemoveField(
            model_name='article',
            name='download_name4',
        ),
        migrations.RemoveField(
            model_name='article',
            name='download_name5',
        ),
    ]
