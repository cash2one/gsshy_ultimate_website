# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsshy', '0005_auto_20160511_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegeprofile',
            name='content',
            field=models.TextField(null=True, verbose_name='\u673a\u6784\u5c55\u793a\u5185\u5bb9', blank=True),
        ),
    ]
