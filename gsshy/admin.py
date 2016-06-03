#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import UserProfile, TopHandoverPicture, NavigationCategory, Category, Subject, Article, Notification,\
    SpecialNews, ImageLink, LinkCategory, Link, CampusPicture, CollegeProfile, ResearchClassfication, \
    Research, ResearchCenterProfile


# Register your models here.

class UserProfileAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', ('last_name', 'first_name'), 'password')}),
        (_(u'个人信息'), {'fields': ('email', 'mobile' )}),
        (_(u'权限设置'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_(u'主要日期'), {'fields': ('last_login', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

    list_display = ('username', 'last_name', 'first_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'last_name', 'first_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('user_permissions',)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'release_unit', 'status')
    search_fields = ('title', 'date_published', 'release_unit__username', 'status')
    ordering = ('-date_published', )
    actions = ['make_published']
    list_per_page = 20
    list_max_show_all = 240

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='yes')
        message_bit = '%s条通知公告' % rows_updated
        self.message_user(request, '%s被成功的标记为已发布状态' % message_bit)
    make_published.short_description = u'标记所选的 通知公告 为已发布状态'

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

# def make_published(modeladmin, request, queryset):
#     queryset.update(status='yes')
# make_published.short_description = u'标记选中的文章为已发布状态'

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'release_unit', 'news_category', 'status')
    search_fields = ('title', 'date_published', 'release_unit__username', 'news_category__name', 'news_category__navigation_category__name', 'status')
    ordering = ('-date_published', )
    actions = ['make_published']
    list_per_page = 20 # 设定每页显示20条数据
    list_max_show_all = 240 # 设定数据全部显示的最大条数为240

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='yes')
        # if rows_updated == 1:
        #     message_bit = "1 story was"
        # else:
        #     message_bit = "%s stories were" % rows_updated
        message_bit = '%s篇文章' % rows_updated
        self.message_user(request, '%s被成功的标记为已发布状态' % message_bit)
    make_published.short_description = u'标记所选的 文章 为已发布状态'

    # 定义ArticleAdmin类的媒体文件.
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

class SpecialNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'release_unit', 'news_category', 'status')
    search_fields = ('title', 'date_published', 'release_unit__username', 'news_category__name', 'status')
    ordering = ('-date_published', )
    actions = ['make_published']
    list_per_page = 20
    list_max_show_all = 240

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='yes')
        messages_bit = '%s篇文章' % rows_updated
        self.message_user(request, '%s被成功的标记为已发布状态' % messages_bit)
    make_published.short_description = u'标记所选的 文章 为已发布状态'

    # 定义SpecialNewsAdmin类的媒体文件.
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

class ResearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'release_unit', 'news_category', 'status')
    search_fields = ('title', 'date_published', 'release_unit__username', 'news_category__name', 'status')
    ordering = ('-date_published', )
    actions = ['make_published']
    list_per_page = 20
    list_max_show_all = 240

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='yes')
        messages_bit = '%s篇文章' % rows_updated
        self.message_user(request, '%s被成功的标记为已发布状态' % messages_bit)
    make_published.short_description = u'标记所选的 文章 为已发布状态'

    # 定义SpecialNewsAdmin类的媒体文件.
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

class CollegeProfileAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )
    ordering = ('id', )
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

class ResearchCenterProfileAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )
    ordering = ('id', )
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(TopHandoverPicture)
admin.site.register(NavigationCategory)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Category)
admin.site.register(Subject)
admin.site.register(Article, ArticleAdmin)
admin.site.register(SpecialNews, SpecialNewsAdmin)
admin.site.register(ResearchClassfication)
admin.site.register(Research, ResearchAdmin)
admin.site.register(ResearchCenterProfile, ResearchCenterProfileAdmin)
admin.site.register(ImageLink)
admin.site.register(LinkCategory)
admin.site.register(Link)
admin.site.register(CampusPicture)
admin.site.register(CollegeProfile, CollegeProfileAdmin)