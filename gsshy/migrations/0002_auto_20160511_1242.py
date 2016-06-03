# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('gsshy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('subtitle', models.CharField(help_text='\u82e5\u8981\u8bbe\u7f6e\u526f\u6807\u9898\uff0c\u8bf7\u6dfb\u52a0\u526f\u6807\u9898', max_length=30, verbose_name='\u526f\u6807\u9898', blank=True)),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('download_file', models.FileField(help_text='\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'file/%Y/%m', null=True, verbose_name='\u9644\u4ef6', blank=True)),
                ('download_name', models.CharField(default='\u4e0b\u8f7d\u6587\u4ef6', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f0')),
                ('date_published', models.DateTimeField(verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('status', models.CharField(default=b'no', max_length=3, verbose_name='\u72b6\u6001', choices=[(b'no', '\u8349\u6848'), (b'yes', '\u5df2\u53d1\u5e03')])),
                ('view_count', models.PositiveIntegerField(default=0, verbose_name='\u6d4f\u89c8\u6b21\u6570')),
                ('index', models.IntegerField(default=999, verbose_name='\u6392\u5217\u987a\u5e8f')),
            ],
            options={
                'ordering': ['-date_published'],
                'verbose_name': '\u7814\u7a76\u4e2d\u5fc3\u8d44\u6599',
                'verbose_name_plural': '\u7814\u7a76\u4e2d\u5fc3\u8d44\u6599',
            },
        ),
        migrations.CreateModel(
            name='ResearchClassfication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name='\u5206\u7c7b\u540d\u79f0')),
                ('index', models.IntegerField(default=999, verbose_name='\u6392\u5217\u987a\u5e8f')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u7814\u7a76\u4e2d\u5fc3\u5206\u7c7b',
                'verbose_name_plural': '\u7814\u7a76\u4e2d\u5fc3\u5206\u7c7b',
            },
        ),
        migrations.AddField(
            model_name='research',
            name='news_category',
            field=models.ForeignKey(verbose_name='\u7814\u7a76\u4e2d\u5fc3\u7c7b\u522b', to='gsshy.ResearchClassfication'),
        ),
        migrations.AddField(
            model_name='research',
            name='release_unit',
            field=models.ForeignKey(verbose_name='\u53d1\u5e03\u5355\u4f4d', to=settings.AUTH_USER_MODEL),
        ),
    ]
