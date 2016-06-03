# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsshy', '0014_auto_20160513_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='news_category',
            field=models.ForeignKey(verbose_name='\u7814\u7a76\u4e2d\u5fc3\u7c7b\u522b', to='gsshy.ResearchClassfication'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(max_length=11, verbose_name='\u624b\u673a\u53f7\u7801', blank=True),
        ),
    ]
