#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    @version: 2.7.10 + 1.8.3
    @author: fangqingsong
    @contact: fqs_1991@yeah.net
    @software: PyCharm
    @file: urls.py
    @time: 16/4/6 16:33
    @license: ...
    @site: ...
"""


from django.conf.urls import url
from .views import index, nav, new, category, introduce, notice, notification, latest_news, \
    search, download, subject, special, research, profile, data

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nav/(?P<nav_id>[0-9]+)/$', nav, name='nav'),
    url(r'^new/(?P<new_id>[0-9]+)/$', new, name='new'),
    url(r'^category/(?P<category_id>[0-9]+)/$', category, name='category'),
    url(r'^introduce/$', introduce, name='introduce'),
    url(r'^notice/$', notice, name='notice'),
    url(r'^notice/(?P<notice_id>[0-9]+)/$', notification, name='notice'),
    url(r'^more/$', latest_news, name='more'),
    url(r'^search/$', search, name='search'),
    url(r'^download/(?P<value>\D+)/(?P<grade>\D+)/(?P<id>[0-9]+)/$', download, name='download'),
    url(r'subject/(?P<subject_id>[0-9]+)/$', subject, name='subject'),
    url(r'special/(?P<special_new_id>[0-9]+)/$', special, name='special'),
    url(r'research/(?P<research_classfication_id>[0-9]+)/$', research, name='research'),
    url(r'profile/(?P<research_center_profile_id>[0-9]+)/$', profile, name='profile'),
    url(r'data/(?P<research_id>[0-9]+)/$', data, name='data'),
]
