#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

# Create your models here.

class UserProfileManager(BaseUserManager):
    """
    自定义用户管理器
    """
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(u'Username必须填写')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True,
                                 **extra_fields)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
        用户
    """
    username = models.CharField(u'用户名', max_length=30, unique=True)
    first_name = models.CharField(u'名字', max_length=30, blank=True)
    last_name = models.CharField(u'姓氏', max_length=30, blank=True)
    email = models.EmailField(u'邮箱', blank=True, null=True)
    is_staff = models.BooleanField(u'职员状态', default=False, help_text='是否能够登录管理后台')
    is_active = models.BooleanField(u'是否激活', default=True, help_text='用户是否被激活，未激活则不能使用')
    date_joined = models.DateTimeField(u'创建日期', auto_now_add=True)
    mobile = models.CharField(u'手机号码', max_length=11, blank=True)

    objects = UserProfileManager()
    class Meta:
        verbose_name = u'管理员'
        verbose_name_plural = verbose_name
        db_table = 'user_profile'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s%s' % (self.last_name, self.first_name)
        return full_name.strip()

    def get_short_name(self):
        'Returns the short name for the user.'
        full_name = '%s%s' % (self.last_name, self.first_name)
        return full_name.strip()


class TopHandoverPicture(models.Model):
    """
        置顶切换图片
    """
    title = models.CharField(u'图片名称', max_length=30)
    description = models.CharField(u'图片描述', max_length=50)
    image = models.ImageField(u'图片', upload_to='top_handover_picture/%Y/%m', blank=True, null=True)
    date_joined = models.DateTimeField(u'添加时间', auto_now_add=True)
    index = models.IntegerField(u'排列顺序', default=999)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'置顶切换图片'
        verbose_name_plural = verbose_name
        ordering = ['id',]


class NavigationCategory(models.Model):
    """
        导航分类
    """
    name = models.CharField(u'导航名称', max_length=30, unique=True)
    index = models.IntegerField(u'排列顺序', default=999)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'导航分类'
        verbose_name_plural = verbose_name
        ordering = ['id',]


class Category(models.Model):
    """
        导航下属小分类
    """
    name = models.CharField(u'分类名称', max_length=30, unique=True)
    navigation_category = models.ForeignKey(NavigationCategory, verbose_name=u'所属导航分类')
    index = models.IntegerField(u'排列顺序', default=999)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = verbose_name
        ordering = ['id',]


class Subject(models.Model):
    """
        专题分类
    """
    name = models.CharField(u'专题名称', max_length=30, unique=True)
    image = models.ImageField(u'专题图片链接', upload_to='subject/%Y/%m', blank=True, null=True)
    index = models.IntegerField(u'排列顺序', default=999)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'专题分类'
        verbose_name_plural = verbose_name
        ordering = ['id',]


class ResearchClassfication(models.Model):
    """
        研究中心分类
    """
    name = models.CharField(u'分类名称', max_length=30, unique=True)
    image = models.ImageField(u'图片链接', upload_to='research_classfication/%Y/%m', blank=True, null=True)
    index = models.IntegerField(u'排列顺序', default=999)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'研究中心分类'
        verbose_name_plural = verbose_name
        ordering = ['id',]


class ResearchCenterProfile(models.Model):
    """
        研究中心简介
    """
    title = models.CharField(u'研究中心名称', max_length=30)
    content = models.TextField(u'研究中心简介内容', blank=True, null=True)
    research_classfication = models.OneToOneField(ResearchClassfication, verbose_name=u'研究中心类别')
    index = models.IntegerField(u'排列顺序', default=999)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'研究中心简介'
        verbose_name_plural = verbose_name
        ordering = ['id',]


class Research(models.Model):
    """
        研究中心资料
    """
    STATUS_CHOICES = (
        ('no', u'草案'),
        ('yes', u'已发布'),
    )
    title = models.CharField(u'标题', max_length=50)
    subtitle = models.CharField(u'副标题', max_length=30, blank=True, help_text=u'若要设置副标题，请添加副标题')
    content = models.TextField(u'内容')
    download_file1 = models.FileField(u'附件1', upload_to='research/%Y/%m', blank=True, null=True, help_text=u'若有下载附件，请添加相关附件')
    download_name1 = models.CharField(u'附件名称1', max_length=50, default=u'下载文件1', help_text=u'若已添加下载附件，请为附件填写名称')
    download_file2 = models.FileField(u'附件2', upload_to='research/%Y/%m', blank=True, null=True, help_text=u'若有下载附件，请添加相关附件')
    download_name2 = models.CharField(u'附件名称2', max_length=50, default=u'下载文件2', help_text=u'若已添加下载附件，请为附件填写名称')
    download_file3 = models.FileField(u'附件3', upload_to='research/%Y/%m', blank=True, null=True, help_text=u'若有下载附件，请添加相关附件')
    download_name3 = models.CharField(u'附件名称3', max_length=50, default=u'下载文件3', help_text=u'若已添加下载附件，请为附件填写名称')
    date_published = models.DateTimeField(u'发布时间')
    release_unit = models.ForeignKey(UserProfile, verbose_name=u'发布单位')
    news_category = models.ForeignKey(ResearchClassfication, verbose_name=u'研究中心类别')
    status = models.CharField(u'状态', max_length=3, choices=STATUS_CHOICES, default='no')
    view_count = models.PositiveIntegerField(u'浏览次数', default=0)
    index = models.IntegerField(u'排列顺序', default=999)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'研究中心资料'
        verbose_name_plural = verbose_name
        ordering = ['-date_published',]


class Notification(models.Model):
    """
        通知
    """
    STATUS_CHOICES = (
        ('no', u'草案'),
        ('yes', u'已发布'),
    )
    title = models.CharField(u'通知标题', max_length=50)
    content = models.TextField(u'通知内容')
    download_file1 = models.FileField(u'附件1', upload_to='notice/%Y/%m', blank=True, null=True, help_text=u'此通知若有下载附件，请添加相关附件')
    download_name1 = models.CharField(u'附件名称1', max_length=50, default=u'下载文件1', help_text=u'若已添加下载附件，请为附件填写名称')
    download_file2 = models.FileField(u'附件2', upload_to='notice/%Y/%m', blank=True, null=True, help_text=u'此通知若有下载附件，请添加相关附件')
    download_name2 = models.CharField(u'附件名称2', max_length=50, default=u'下载文件2', help_text=u'若已添加下载附件，请为附件填写名称')
    download_file3 = models.FileField(u'附件3', upload_to='notice/%Y/%m', blank=True, null=True, help_text=u'此通知若有下载附件，请添加相关附件')
    download_name3 = models.CharField(u'附件名称3', max_length=50, default=u'下载文件3', help_text=u'若已添加下载附件，请为附件填写名称')
    date_published = models.DateTimeField(u'发布时间')
    release_unit = models.ForeignKey(UserProfile, verbose_name=u'发布单位')
    status = models.CharField(u'通知公告状态', max_length=3, choices=STATUS_CHOICES, default='no')
    view_count = models.PositiveIntegerField(u'浏览次数', default=0)
    index = models.IntegerField(u'排列顺序', default=999)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'通知公告'
        verbose_name_plural = verbose_name
        ordering = ['-date_published',]


class Article(models.Model):
    """
        新闻
    """
    STATUS_CHOICES = (
        ('no', u'草案'),
        ('yes', u'已发布'),
    )
    title = models.CharField(u'新闻标题', max_length=50)
    subtitle = models.CharField(u'副标题', max_length=30, blank=True, help_text=u'此新闻若要设置副标题，请添加新闻副标题')
    image_url = models.ImageField(u'新闻标题图片', upload_to='article/%Y/%m', blank=True, null=True, help_text=u'此新闻若要在首页轮播展示，请添加标题展示图片')
    content = models.TextField(u'新闻内容', blank=True, null=True)
    download_file1 = models.FileField(u'附件1', upload_to='file/%Y/%m', blank=True, null=True, help_text=u'此新闻若有下载附件，请添加相关附件')
    download_name1 = models.CharField(u'附件名称1', max_length=50, default=u'下载文件1', help_text=u'若已添加下载附件，请为附件填写名称')
    download_file2 = models.FileField(u'附件2', upload_to='file/%Y/%m', blank=True, null=True, help_text=u'此新闻若有下载附件，请添加相关附件')
    download_name2 = models.CharField(u'附件名称2', max_length=50, default=u'下载文件2', help_text=u'若已添加下载附件，请为附件填写名称')
    download_file3 = models.FileField(u'附件3', upload_to='file/%Y/%m', blank=True, null=True, help_text=u'此新闻若有下载附件，请添加相关附件')
    download_name3 = models.CharField(u'附件名称3', max_length=50, default=u'下载文件3', help_text=u'若已添加下载附件，请为附件填写名称')
    date_published = models.DateTimeField(u'发布时间')
    release_unit = models.ForeignKey(UserProfile, verbose_name=u'发布单位')
    news_category = models.ForeignKey(Category, verbose_name=u'新闻类别')
    status = models.CharField(u'文章状态', max_length=3, choices=STATUS_CHOICES, default='no')
    view_count = models.PositiveIntegerField(u'浏览次数', default=0)
    index = models.IntegerField(u'排列顺序', default=999)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_published',]


class SpecialNews(models.Model):
    """
        专题新闻
    """
    STATUS_CHOICES = (
        ('no', u'草案'),
        ('yes', u'已发布'),
    )
    title = models.CharField(u'专题新闻标题', max_length=50)
    subtitle = models.CharField(u'副标题', max_length=30, blank=True, help_text=u'此专题新闻若要设置副标题，请添加专题新闻副标题')
    content = models.TextField(u'专题新闻内容')
    download_file1 = models.FileField(u'附件1', upload_to='subjectfile/%Y/%m', blank=True, null=True, help_text=u'此专题新闻若有下载附件，请添加相关附件')
    download_name1 = models.CharField(u'附件名称1', max_length=50, default=u'下载文件1', help_text=u'若已添加下载附件，请为附件填写名称')
    download_file2 = models.FileField(u'附件2', upload_to='subjectfile/%Y/%m', blank=True, null=True, help_text=u'此专题新闻若有下载附件，请添加相关附件')
    download_name2 = models.CharField(u'附件名称2', max_length=50, default=u'下载文件2', help_text=u'若已添加下载附件，请为附件填写名称')
    download_file3 = models.FileField(u'附件3', upload_to='subjectfile/%Y/%m', blank=True, null=True, help_text=u'此专题新闻若有下载附件，请添加相关附件')
    download_name3 = models.CharField(u'附件名称3', max_length=50, default=u'下载文件3', help_text=u'若已添加下载附件，请为附件填写名称')
    date_published = models.DateTimeField(u'发布时间')
    release_unit = models.ForeignKey(UserProfile, verbose_name=u'发布单位')
    news_category = models.ForeignKey(Subject, verbose_name=u'专题类别')
    status = models.CharField(u'文章状态', max_length=3, choices=STATUS_CHOICES, default='no')
    view_count = models.PositiveIntegerField(u'浏览次数', default=0)
    index = models.IntegerField(u'排列顺序', default=999)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'专题文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_published',]


class CollegeProfile(models.Model):
    """
        学院概况
    """
    title = models.CharField(u'机构名称', max_length=30)
    content = models.TextField(u'机构展示内容', blank=True, null=True)
    index = models.IntegerField(u'排列顺序', default=999)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'学院概况'
        verbose_name_plural = verbose_name
        ordering = ['id',]

class CampusPicture(models.Model):
    """
        校园风采图片
    """
    title = models.CharField(u'图片名称', max_length=30)
    description = models.CharField(u'图片描述', max_length=30)
    image_url = models.ImageField(u'图片', upload_to='campus_picture/%Y/%m',)
    date_joined = models.DateTimeField(u'添加时间', auto_now_add=True)
    index = models.IntegerField(u'排列顺序', default=999)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'校园风采图片'
        verbose_name_plural = verbose_name
        ordering = ['id',]


class ImageLink(models.Model):
    """
        图标链接
    """
    title = models.CharField(u'图标链接名称', max_length=30, unique=True)
    image = models.ImageField(u'图标', upload_to='imagelink/%Y/%m', blank=True, null=True)
    description = models.CharField(u'图标链接描述', max_length=50)
    callback_url = models.URLField(u'回调地址')
    date_joined = models.DateTimeField(u'添加时间', auto_now_add=True)
    index = models.IntegerField(u'排列顺序', default=999)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'图标链接'
        verbose_name_plural = verbose_name
        ordering = ['id',]


class LinkCategory(models.Model):
    """
        友情链接分类
    """
    name = models.CharField(u'链接分类名称', max_length=30, unique=True)
    index = models.IntegerField(u'排列顺序', default=999)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'友情链接分类'
        verbose_name_plural = verbose_name
        ordering = ['id',]

class Link(models.Model):
    """
        友情链接
    """
    title = models.CharField(u'链接名称', max_length=30, unique=True)
    description = models.CharField(u'链接描述', max_length=50)
    callback_url = models.URLField(u'回调地址')
    date_joined = models.DateTimeField(u'添加时间', auto_now_add=True)
    link_category = models.ForeignKey(LinkCategory, verbose_name=u'链接类别')
    index = models.IntegerField(u'排列顺序', default=999)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'友情链接'
        verbose_name_plural = verbose_name
        ordering = ['id',]
