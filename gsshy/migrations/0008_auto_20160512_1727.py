# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsshy', '0007_subject_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='download_file',
        ),
        migrations.RemoveField(
            model_name='article',
            name='download_name',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='download_file',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='download_name',
        ),
        migrations.RemoveField(
            model_name='research',
            name='download_file',
        ),
        migrations.RemoveField(
            model_name='research',
            name='download_name',
        ),
        migrations.RemoveField(
            model_name='specialnews',
            name='download_file',
        ),
        migrations.RemoveField(
            model_name='specialnews',
            name='download_name',
        ),
        migrations.AddField(
            model_name='article',
            name='download_file1',
            field=models.FileField(help_text='\u6b64\u65b0\u95fb\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'file/%Y/%m', null=True, verbose_name='\u9644\u4ef61', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='download_file2',
            field=models.FileField(help_text='\u6b64\u65b0\u95fb\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'file/%Y/%m', null=True, verbose_name='\u9644\u4ef62', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='download_file3',
            field=models.FileField(help_text='\u6b64\u65b0\u95fb\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'file/%Y/%m', null=True, verbose_name='\u9644\u4ef63', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='download_file4',
            field=models.FileField(help_text='\u6b64\u65b0\u95fb\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'file/%Y/%m', null=True, verbose_name='\u9644\u4ef64', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='download_file5',
            field=models.FileField(help_text='\u6b64\u65b0\u95fb\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'file/%Y/%m', null=True, verbose_name='\u9644\u4ef65', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='download_name1',
            field=models.CharField(default='\u4e0b\u8f7d\u6587\u4ef61', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f01'),
        ),
        migrations.AddField(
            model_name='article',
            name='download_name2',
            field=models.CharField(default='\u4e0b\u8f7d\u6587\u4ef62', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f02'),
        ),
        migrations.AddField(
            model_name='article',
            name='download_name3',
            field=models.CharField(default='\u4e0b\u8f7d\u6587\u4ef63', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f03'),
        ),
        migrations.AddField(
            model_name='article',
            name='download_name4',
            field=models.CharField(default='\u4e0b\u8f7d\u6587\u4ef64', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f04'),
        ),
        migrations.AddField(
            model_name='article',
            name='download_name5',
            field=models.CharField(default='\u4e0b\u8f7d\u6587\u4ef65', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f05'),
        ),
        migrations.AddField(
            model_name='notification',
            name='download_file1',
            field=models.FileField(help_text='\u6b64\u901a\u77e5\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'notice/%Y/%m', null=True, verbose_name='\u9644\u4ef61', blank=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='download_file2',
            field=models.FileField(help_text='\u6b64\u901a\u77e5\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'notice/%Y/%m', null=True, verbose_name='\u9644\u4ef62', blank=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='download_file3',
            field=models.FileField(help_text='\u6b64\u901a\u77e5\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'notice/%Y/%m', null=True, verbose_name='\u9644\u4ef63', blank=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='download_name1',
            field=models.CharField(default='\u4e0b\u8f7d\u6587\u4ef61', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f01'),
        ),
        migrations.AddField(
            model_name='notification',
            name='download_name2',
            field=models.CharField(default='\u4e0b\u8f7d\u6587\u4ef62', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f02'),
        ),
        migrations.AddField(
            model_name='notification',
            name='download_name3',
            field=models.CharField(default='\u4e0b\u8f7d\u6587\u4ef63', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f03'),
        ),
        migrations.AddField(
            model_name='research',
            name='download_file1',
            field=models.FileField(help_text='\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'research/%Y/%m', null=True, verbose_name='\u9644\u4ef61', blank=True),
        ),
        migrations.AddField(
            model_name='research',
            name='download_file2',
            field=models.FileField(help_text='\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'research/%Y/%m', null=True, verbose_name='\u9644\u4ef62', blank=True),
        ),
        migrations.AddField(
            model_name='research',
            name='download_file3',
            field=models.FileField(help_text='\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'research/%Y/%m', null=True, verbose_name='\u9644\u4ef63', blank=True),
        ),
        migrations.AddField(
            model_name='research',
            name='download_name1',
            field=models.CharField(default='\u4e0b\u8f7d\u6587\u4ef61', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f01'),
        ),
        migrations.AddField(
            model_name='research',
            name='download_name2',
            field=models.CharField(default='\u4e0b\u8f7d\u6587\u4ef62', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f02'),
        ),
        migrations.AddField(
            model_name='research',
            name='download_name3',
            field=models.CharField(default='\u4e0b\u8f7d\u6587\u4ef63', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f03'),
        ),
        migrations.AddField(
            model_name='specialnews',
            name='download_file1',
            field=models.FileField(help_text='\u6b64\u4e13\u9898\u65b0\u95fb\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'subjectfile/%Y/%m', null=True, verbose_name='\u9644\u4ef61', blank=True),
        ),
        migrations.AddField(
            model_name='specialnews',
            name='download_file2',
            field=models.FileField(help_text='\u6b64\u4e13\u9898\u65b0\u95fb\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'subjectfile/%Y/%m', null=True, verbose_name='\u9644\u4ef62', blank=True),
        ),
        migrations.AddField(
            model_name='specialnews',
            name='download_file3',
            field=models.FileField(help_text='\u6b64\u4e13\u9898\u65b0\u95fb\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'subjectfile/%Y/%m', null=True, verbose_name='\u9644\u4ef63', blank=True),
        ),
        migrations.AddField(
            model_name='specialnews',
            name='download_name1',
            field=models.CharField(default='\u4e0b\u8f7d\u6587\u4ef61', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f01'),
        ),
        migrations.AddField(
            model_name='specialnews',
            name='download_name2',
            field=models.CharField(default='\u4e0b\u8f7d\u6587\u4ef62', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f02'),
        ),
        migrations.AddField(
            model_name='specialnews',
            name='download_name3',
            field=models.CharField(default='\u4e0b\u8f7d\u6587\u4ef63', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f03'),
        ),
    ]
