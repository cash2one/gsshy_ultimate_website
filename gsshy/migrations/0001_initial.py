# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(unique=True, max_length=30, verbose_name='\u7528\u6237\u540d')),
                ('first_name', models.CharField(max_length=30, verbose_name='\u540d\u5b57', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='\u59d3\u6c0f', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='\u90ae\u7bb1', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text=b'\xe6\x98\xaf\xe5\x90\xa6\xe8\x83\xbd\xe5\xa4\x9f\xe7\x99\xbb\xe5\xbd\x95\xe7\xae\xa1\xe7\x90\x86\xe5\x90\x8e\xe5\x8f\xb0', verbose_name='\u804c\u5458\u72b6\u6001')),
                ('is_active', models.BooleanField(default=True, help_text=b'\xe7\x94\xa8\xe6\x88\xb7\xe6\x98\xaf\xe5\x90\xa6\xe8\xa2\xab\xe6\xbf\x80\xe6\xb4\xbb\xef\xbc\x8c\xe6\x9c\xaa\xe6\xbf\x80\xe6\xb4\xbb\xe5\x88\x99\xe4\xb8\x8d\xe8\x83\xbd\xe4\xbd\xbf\xe7\x94\xa8', verbose_name='\u662f\u5426\u6fc0\u6d3b')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65e5\u671f')),
                ('mobile', models.CharField(max_length=11, null=True, verbose_name='\u624b\u673a\u53f7\u7801', blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user_profile',
                'verbose_name': '\u7ba1\u7406\u5458',
                'verbose_name_plural': '\u7ba1\u7406\u5458',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u65b0\u95fb\u6807\u9898')),
                ('subtitle', models.CharField(help_text='\u6b64\u65b0\u95fb\u82e5\u8981\u8bbe\u7f6e\u526f\u6807\u9898\uff0c\u8bf7\u6dfb\u52a0\u65b0\u95fb\u526f\u6807\u9898', max_length=30, verbose_name='\u526f\u6807\u9898', blank=True)),
                ('image_url', models.ImageField(help_text='\u6b64\u65b0\u95fb\u82e5\u8981\u5728\u9996\u9875\u8f6e\u64ad\u5c55\u793a\uff0c\u8bf7\u6dfb\u52a0\u6807\u9898\u5c55\u793a\u56fe\u7247', upload_to=b'article/%Y/%m', null=True, verbose_name='\u65b0\u95fb\u6807\u9898\u56fe\u7247', blank=True)),
                ('content', models.TextField(verbose_name='\u65b0\u95fb\u5185\u5bb9')),
                ('download_file', models.FileField(help_text='\u6b64\u65b0\u95fb\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'file/%Y/%m', null=True, verbose_name='\u9644\u4ef6', blank=True)),
                ('download_name', models.CharField(default='\u4e0b\u8f7d\u6587\u4ef6', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f0')),
                ('date_published', models.DateTimeField(verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('status', models.CharField(default=b'no', max_length=3, verbose_name='\u6587\u7ae0\u72b6\u6001', choices=[(b'no', '\u8349\u6848'), (b'yes', '\u5df2\u53d1\u5e03')])),
                ('view_count', models.PositiveIntegerField(default=0, verbose_name='\u6d4f\u89c8\u6b21\u6570')),
                ('index', models.IntegerField(default=999, verbose_name='\u6392\u5217\u987a\u5e8f')),
            ],
            options={
                'ordering': ['-date_published'],
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='CampusPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name='\u56fe\u7247\u540d\u79f0')),
                ('description', models.CharField(max_length=30, verbose_name='\u56fe\u7247\u63cf\u8ff0')),
                ('image_url', models.ImageField(upload_to=b'campus_picture/%Y/%m', verbose_name='\u56fe\u7247')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('index', models.IntegerField(default=999, verbose_name='\u6392\u5217\u987a\u5e8f')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u6821\u56ed\u98ce\u91c7\u56fe\u7247',
                'verbose_name_plural': '\u6821\u56ed\u98ce\u91c7\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name='\u5206\u7c7b\u540d\u79f0')),
                ('index', models.IntegerField(default=999, verbose_name='\u6392\u5217\u987a\u5e8f')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='CollegeProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name='\u673a\u6784\u540d\u79f0')),
                ('content', models.TextField(verbose_name='\u673a\u6784\u5c55\u793a\u5185\u5bb9')),
                ('index', models.IntegerField(default=999, verbose_name='\u6392\u5217\u987a\u5e8f')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u5b66\u9662\u6982\u51b5',
                'verbose_name_plural': '\u5b66\u9662\u6982\u51b5',
            },
        ),
        migrations.CreateModel(
            name='ImageLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=30, verbose_name='\u56fe\u6807\u94fe\u63a5\u540d\u79f0')),
                ('description', models.CharField(max_length=50, verbose_name='\u56fe\u6807\u94fe\u63a5\u63cf\u8ff0')),
                ('callback_url', models.URLField(verbose_name='\u56de\u8c03\u5730\u5740')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('index', models.IntegerField(default=999, verbose_name='\u6392\u5217\u987a\u5e8f')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u56fe\u6807\u94fe\u63a5',
                'verbose_name_plural': '\u56fe\u6807\u94fe\u63a5',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=30, verbose_name='\u94fe\u63a5\u540d\u79f0')),
                ('description', models.CharField(max_length=50, verbose_name='\u94fe\u63a5\u63cf\u8ff0')),
                ('callback_url', models.URLField(verbose_name='\u56de\u8c03\u5730\u5740')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('index', models.IntegerField(default=999, verbose_name='\u6392\u5217\u987a\u5e8f')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u53cb\u60c5\u94fe\u63a5',
                'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5',
            },
        ),
        migrations.CreateModel(
            name='LinkCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name='\u94fe\u63a5\u5206\u7c7b\u540d\u79f0')),
                ('index', models.IntegerField(default=999, verbose_name='\u6392\u5217\u987a\u5e8f')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u53cb\u60c5\u94fe\u63a5\u5206\u7c7b',
                'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='NavigationCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name='\u5bfc\u822a\u540d\u79f0')),
                ('index', models.IntegerField(default=999, verbose_name='\u6392\u5217\u987a\u5e8f')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u5bfc\u822a\u5206\u7c7b',
                'verbose_name_plural': '\u5bfc\u822a\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u901a\u77e5\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u901a\u77e5\u5185\u5bb9')),
                ('download_file', models.FileField(help_text='\u6b64\u901a\u77e5\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'notice/%Y/%m', null=True, verbose_name='\u9644\u4ef6', blank=True)),
                ('download_name', models.CharField(default='\u4e0b\u8f7d\u6587\u4ef6', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f0')),
                ('date_published', models.DateTimeField(verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('status', models.CharField(default=b'no', max_length=3, verbose_name='\u901a\u77e5\u516c\u544a\u72b6\u6001', choices=[(b'no', '\u8349\u6848'), (b'yes', '\u5df2\u53d1\u5e03')])),
                ('view_count', models.PositiveIntegerField(default=0, verbose_name='\u6d4f\u89c8\u6b21\u6570')),
                ('index', models.IntegerField(default=999, verbose_name='\u6392\u5217\u987a\u5e8f')),
                ('release_unit', models.ForeignKey(verbose_name='\u53d1\u5e03\u5355\u4f4d', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_published'],
                'verbose_name': '\u901a\u77e5\u516c\u544a',
                'verbose_name_plural': '\u901a\u77e5\u516c\u544a',
            },
        ),
        migrations.CreateModel(
            name='SpecialNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u4e13\u9898\u65b0\u95fb\u6807\u9898')),
                ('subtitle', models.CharField(help_text='\u6b64\u4e13\u9898\u65b0\u95fb\u82e5\u8981\u8bbe\u7f6e\u526f\u6807\u9898\uff0c\u8bf7\u6dfb\u52a0\u4e13\u9898\u65b0\u95fb\u526f\u6807\u9898', max_length=30, verbose_name='\u526f\u6807\u9898', blank=True)),
                ('content', models.TextField(verbose_name='\u4e13\u9898\u65b0\u95fb\u5185\u5bb9')),
                ('download_file', models.FileField(help_text='\u6b64\u4e13\u9898\u65b0\u95fb\u82e5\u6709\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u6dfb\u52a0\u76f8\u5173\u9644\u4ef6', upload_to=b'subjectfile/%Y/%m', null=True, verbose_name='\u9644\u4ef6', blank=True)),
                ('download_name', models.CharField(default='\u4e0b\u8f7d\u6587\u4ef6', help_text='\u82e5\u5df2\u6dfb\u52a0\u4e0b\u8f7d\u9644\u4ef6\uff0c\u8bf7\u4e3a\u9644\u4ef6\u586b\u5199\u540d\u79f0', max_length=50, verbose_name='\u9644\u4ef6\u540d\u79f0')),
                ('date_published', models.DateTimeField(verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('status', models.CharField(default=b'no', max_length=3, verbose_name='\u6587\u7ae0\u72b6\u6001', choices=[(b'no', '\u8349\u6848'), (b'yes', '\u5df2\u53d1\u5e03')])),
                ('view_count', models.PositiveIntegerField(default=0, verbose_name='\u6d4f\u89c8\u6b21\u6570')),
                ('index', models.IntegerField(default=999, verbose_name='\u6392\u5217\u987a\u5e8f')),
            ],
            options={
                'ordering': ['-date_published'],
                'verbose_name': '\u4e13\u9898\u6587\u7ae0',
                'verbose_name_plural': '\u4e13\u9898\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name='\u4e13\u9898\u540d\u79f0')),
                ('index', models.IntegerField(default=999, verbose_name='\u6392\u5217\u987a\u5e8f')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u4e13\u9898\u5206\u7c7b',
                'verbose_name_plural': '\u4e13\u9898\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='TopHandoverPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name='\u56fe\u7247\u540d\u79f0')),
                ('description', models.CharField(max_length=50, verbose_name='\u56fe\u7247\u63cf\u8ff0')),
                ('image', models.ImageField(upload_to=b'top_handover_picture/%Y/%m', null=True, verbose_name='\u56fe\u7247', blank=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('index', models.IntegerField(default=999, verbose_name='\u6392\u5217\u987a\u5e8f')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u7f6e\u9876\u5207\u6362\u56fe\u7247',
                'verbose_name_plural': '\u7f6e\u9876\u5207\u6362\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='VideoProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('title_image', models.ImageField(upload_to=b'video_pic/%Y/%m', verbose_name='\u6807\u9898\u56fe\u7247')),
                ('video', models.FileField(upload_to=b'video/%Y/%m', verbose_name='\u89c6\u9891\u6587\u4ef6')),
                ('date_published', models.DateTimeField(verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('view_count', models.PositiveIntegerField(default=0, verbose_name='\u6d4f\u89c8\u6b21\u6570')),
                ('index', models.IntegerField(default=999, verbose_name='\u6392\u5217\u987a\u5e8f')),
                ('release_unit', models.ForeignKey(verbose_name='\u53d1\u5e03\u5355\u4f4d', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u89c6\u9891\u6587\u4ef6',
                'verbose_name_plural': '\u89c6\u9891\u6587\u4ef6',
            },
        ),
        migrations.AddField(
            model_name='specialnews',
            name='news_category',
            field=models.ForeignKey(verbose_name='\u4e13\u9898\u7c7b\u522b', to='gsshy.Subject'),
        ),
        migrations.AddField(
            model_name='specialnews',
            name='release_unit',
            field=models.ForeignKey(verbose_name='\u53d1\u5e03\u5355\u4f4d', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='link',
            name='link_category',
            field=models.ForeignKey(verbose_name='\u94fe\u63a5\u7c7b\u522b', to='gsshy.LinkCategory'),
        ),
        migrations.AddField(
            model_name='category',
            name='navigation_category',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u5bfc\u822a\u5206\u7c7b', to='gsshy.NavigationCategory'),
        ),
        migrations.AddField(
            model_name='article',
            name='news_category',
            field=models.ForeignKey(verbose_name='\u65b0\u95fb\u7c7b\u522b', to='gsshy.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='release_unit',
            field=models.ForeignKey(verbose_name='\u53d1\u5e03\u5355\u4f4d', to=settings.AUTH_USER_MODEL),
        ),
    ]
