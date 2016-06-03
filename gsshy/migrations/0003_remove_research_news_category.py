# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsshy', '0002_auto_20160511_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research',
            name='news_category',
        ),
    ]
