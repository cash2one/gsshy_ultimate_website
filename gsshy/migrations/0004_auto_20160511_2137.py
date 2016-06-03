# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsshy', '0003_remove_research_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='news_category',
            field=models.ForeignKey(verbose_name='\u7814\u7a76\u4e2d\u5fc3\u7c7b\u522b', blank=True, to='gsshy.ResearchClassfication', null=True),
        ),
        migrations.AddField(
            model_name='researchclassfication',
            name='image',
            field=models.ImageField(upload_to=b'research_classfication/%Y/%m', null=True, verbose_name='\u56fe\u7247\u94fe\u63a5', blank=True),
        ),
    ]
