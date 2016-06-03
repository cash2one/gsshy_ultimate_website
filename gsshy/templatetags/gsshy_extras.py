#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from django import template
from django.utils import timezone
import time

register = template.Library()

@register.filter(expects_localtime=True)
def is_new(value):
    # python2.7 获取时间戳的方式
    date_published_timestamp = int(time.mktime(value.timetuple()))
    now_timestamp = int(time.mktime(timezone.now().timetuple()))
    seconds = now_timestamp - date_published_timestamp
    seconds_of_two_month = 2*30*24*60*60

    if seconds <= seconds_of_two_month:
        return True
    else:
        return False