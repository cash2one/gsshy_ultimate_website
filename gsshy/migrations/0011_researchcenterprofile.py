# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsshy', '0010_imagelink_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchCenterProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name='\u7814\u7a76\u4e2d\u5fc3\u540d\u79f0')),
                ('content', models.TextField(null=True, verbose_name='\u7814\u7a76\u4e2d\u5fc3\u7b80\u4ecb\u5185\u5bb9', blank=True)),
                ('index', models.IntegerField(default=999, verbose_name='\u6392\u5217\u987a\u5e8f')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u7814\u7a76\u4e2d\u5fc3\u7b80\u4ecb',
                'verbose_name_plural': '\u7814\u7a76\u4e2d\u5fc3\u7b80\u4ecb',
            },
        ),
    ]
