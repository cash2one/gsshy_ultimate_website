# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsshy', '0004_auto_20160511_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(null=True, verbose_name='\u65b0\u95fb\u5185\u5bb9', blank=True),
        ),
    ]
