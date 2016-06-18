#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.http import StreamingHttpResponse
from .models import *
from django.utils import timezone
from django.conf import settings

import logging
import time
import re
import os

# Create your views here.

# 定义日志器
logger = logging.getLogger('gsshy.views')

# 已发布的全部文章
published_articles = None

# 已发布的全部通知公告
published_notifications = None

# 已发布的专题文章
published_subject_news = None

# 已发布的研究中心文章
published_researches = None

# 研究中心分类
research_classfications = None

# 研究中心简介
research_center_profiles = None

# 判断是否为最新文章(60天)
def is_latest_article(request, date):
    date_published_timestamp = int(time.mktime(date.timetuple()))
    now_timestamp = int(time.mktime(timezone.now().timetuple()))
    seconds = now_timestamp - date_published_timestamp
    seconds_of_two_month = 2*30*24*60*60

    if seconds <= seconds_of_two_month:
        return True
    else:
        return False

def global_setting(request):
    global published_articles, published_notifications, published_subject_news, published_researches, research_center_profiles, research_classfications
    try:

        STATIC_URL = settings.STATIC_URL
        MEDIA_URL = settings.MEDIA_URL

        # 置顶图片
        top_handover_pics = TopHandoverPicture.objects.all()

        # 导航分类
        navigation_category_list = NavigationCategory.objects.all()

         # 分类(因为研究中心的导航分类与其他的导航分类在处理方式上存在差异,所以对此另作处理,对研究中心导航分类
         # 下的五个小分类分别动态赋予key的值,以此在前端页面的url中进行传值)
        categories = Category.objects.filter(navigation_category__name=u'研究中心')

        for cate in categories:
            if cate.name == u'统战理论':
                cate.key = 1
            elif cate.name == u'民族宗教':
                cate.key = 2
            elif cate.name == u'新的社会阶层':
                cate.key = 3
            elif cate.name == u'智库联盟社院':
                cate.key = 4
            else:
                cate.key = 5

        # 所有已发布的通知公告
        published_notifications = Notification.objects.filter(status='yes')
        notifications = published_notifications[0:10]

        # 所有已发布的文章
        published_articles = Article.objects.filter(status='yes')

        # 所有已发布的专题文章
        published_subject_news = SpecialNews.objects.filter(status='yes')

        # 所有已发布的研究中心文章
        published_researches = Research.objects.filter(status='yes')

        # 获取研究中心简介
        research_center_profiles = ResearchCenterProfile.objects.all()

        # 图片链接
        imagelinks = ImageLink.objects.all()

        # 图片标题新闻，设置最多显示4条新闻
        photo_headline_news_temp = [article for article in published_articles if article.image_url]
        photo_headline_news_count = len(photo_headline_news_temp)
        
        if photo_headline_news_count <= 4:
            photo_headline_news = photo_headline_news_temp
        else:
            photo_headline_news = photo_headline_news_temp[0:4]

        # 新闻中心列表，包含统战要闻、社院新闻、市州社院动态三个分类的新闻，显示面最多显示7条新闻
        news_list = list()

        tongzhan_news = published_articles.filter(news_category__name=u'统战要闻')[0:7]
        tongzhan_news.index = 1
        tongzhan_news.display = 1
        tongzhan_news.id = Category.objects.get(name=u'统战要闻').id
        news_list.append(tongzhan_news)

        sheyuan_news = published_articles.filter(news_category__name=u'社院新闻')[0:7]
        sheyuan_news.index = 2
        sheyuan_news.display = 0
        sheyuan_news.id = Category.objects.get(name=u'社院新闻').id
        news_list.append(sheyuan_news)

        shizhou_news = published_articles.filter(news_category__name=u'市州社院')[0:7]
        shizhou_news.index = 3
        shizhou_news.display = 0
        shizhou_news.id = Category.objects.get(name=u'市州社院').id
        news_list.append(shizhou_news)
        xinwen_zhongxin_id = NavigationCategory.objects.get(name=u'新闻中心').id


        # 获取学院概况下面除学院简介外的分类
        college_categories = Category.objects.filter(navigation_category__name=u'学院概况').exclude(name=u'学院简介')

        # 党务政务的新闻列表，因为这里的导航栏与分类都设置的是党务政务所以直接用分类标识
        dangwu_news = published_articles.filter(news_category__name=u'党务政务')[0:11]
        dangwu_news.id = NavigationCategory.objects.get(name=u'党务政务').id

        # 获取所属教学培训导航栏的新闻列表
        jiaoxue_news = published_articles.filter(news_category__navigation_category__name=u'教学培训')[0:11]
        jiaoxue_news.id = NavigationCategory.objects.get(name=u'教学培训').id

        # 获取所属科研工作导航栏的新闻列表
        keyan_news = published_articles.filter(news_category__navigation_category__name=u'科研工作')[0:11]
        keyan_news.id = NavigationCategory.objects.get(name=u'科研工作').id

        # 获取所属文化交流导航栏的新闻列表
        wenhua_news = published_articles.filter(news_category__navigation_category__name=u'文化交流')[0:11]
        wenhua_news.id = NavigationCategory.objects.get(name=u'文化交流').id

        # 获取所属后勤服务导航栏的新闻列表
        houqin_news = published_articles.filter(news_category__navigation_category__name=u'后勤服务')[0:11]
        houqin_news.id = NavigationCategory.objects.get(name=u'后勤服务').id

        # 获取校园风采图片列表
        campus_picture_list = CampusPicture.objects.all()

        # 获取研究中心分类列表并做相应的处理
        research_classfications = ResearchClassfication.objects.all()
        number = 1

        research_classfication_list = list()
        research_classfication_obj = research_classfications.get(name=u'统战理论研究中心')
        research_classfication_obj.key = 1
        research_classfication_obj.index = 1
        research_classfication_list.append(research_classfication_obj)

        classfications = research_classfications.exclude(name=u'统战理论研究中心')
        for c in classfications:
            number += 1
            c.index = 2
            c.key = number
            research_classfication_list.append(c)

        # 获取专题分类列表
        subjects = Subject.objects.all()

        # 链接导航列表，包含主要媒体、统战系统、各省社院、市州社院
        links = Link.objects.all()

        links_list = list()

        meiti_links = links.filter(link_category__name=u'主要媒体')
        meiti_links.index = 1
        meiti_links.display = 1
        meiti_links.id = LinkCategory.objects.get(name=u'主要媒体').id
        links_list.append(meiti_links)

        tongzhan_links = links.filter(link_category__name=u'统战系统')
        tongzhan_links.index = 2
        tongzhan_links.display = 0
        tongzhan_links.id = LinkCategory.objects.get(name=u'统战系统').id
        links_list.append(tongzhan_links)

        gesheng_links = links.filter(link_category__name=u'各省社院')
        gesheng_links.index = 3
        gesheng_links.display = 0
        gesheng_links.id = LinkCategory.objects.get(name=u'各省社院').id
        links_list.append(gesheng_links)

        shizhou_links = links.filter(link_category__name=u'市州社院')
        shizhou_links.index = 4
        shizhou_links.display = 0
        shizhou_links.id = LinkCategory.objects.get(name=u'市州社院').id
        links_list.append(shizhou_links)

        # 获取最新文章
        latest_publish_news = [article for article in published_articles if is_latest_article(request, article.date_published)][0:8]

    except Exception as e:
        logger.error(e)

    return locals()

# 首页
def index(request):

    # import socket
    # print socket.gethostname()

    return render(request, 'index.html', locals())

# 学院简介
def introduce(request):
    return render(request, 'introduce.html', locals())

# 分页代码
def get_page(request, new_list):
    paginator = Paginator(new_list, 16)
    try:
        page = int(request.GET.get('page', 1))
        new_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        new_list = paginator.page(1)
    return new_list

# 获取搜索的结果
def get_search_results(request, word):
    pattern_year_month_date = r'^(\d{4})-(0[1-9]{1}|1[0-2])-(0[1-9]{1}|[12]\d{1}|3[01])$'
    pattern_year_month = r'^(\d{4})-(0[1-9]{1}|1[0-2])$'
    pattern_year = r'^(\d{4})$'

    if re.match(pattern_year_month_date, word):
        results = list(published_articles.filter(date_published__contains=word))
    elif re.match(pattern_year_month, word):
        results = list(published_articles.filter(date_published__contains=word))
    elif re.match(pattern_year, word):
        title_results = list(published_articles.filter(title__icontains=word))
        date_results = list(published_articles.filter(date_published__contains=word))
        temp_results = set(title_results + date_results)
        results = [r for r in temp_results]
        def date_desc(obja, objb): # 定义时间降序函数
            if obja.date_published < objb.date_published:
                return 1
            elif obja.date_published > objb.date_published:
                return -1
            else:
                return 0
        results.sort(cmp=date_desc)
    else:
        results = list(published_articles.filter(title__icontains=word))

    return results

search_results = None

# 搜索
def search(request):
    global search_results
    try:
        if request.method == 'POST':
            keyword = request.POST.get('keyword', None)
            if keyword:
                keyword = keyword.strip()
                search_results = get_search_results(request, keyword)
                results = get_page(request, search_results)
                return render(request, 'search_list.html', locals())
        else:
            results = get_page(request, search_results)
            return render(request, 'search_list.html', locals())
    except Exception as e:
        logger.error(e)
    return render(request, 'index.html', locals())

# 导航栏
def nav(request, nav_id):
    try:
        nav_category_obj = NavigationCategory.objects.get(pk=nav_id)
        nav_category_name = nav_category_obj.name

        if nav_category_name == u'学院概况' or nav_category_name == u'研究中心' or nav_category_name == u'数字社院':
            return render(request, 'index.html')
        else:
            news = published_articles.filter(news_category__navigation_category__id=nav_id)
            news = get_page(request, news)
            news.nav = nav_category_obj #将导航栏这个对象动态赋值给news列表
            return render(request, 'new_list.html', locals())
    except Exception as e:
        logger.error(e)
        return render(request, 'index.html', locals())

# 公告
def notice(request):
    try:
        notifications = get_page(request, published_notifications)
        return render(request, 'notification_list.html', locals())
    except Exception as e:
        logger.error(e)
        return render(request, 'index.html', locals())

# 上一篇与下一篇的辅助函数
def assistant(request, obj, id_list, model):
    id_list_count = len(id_list)
    last_id_index = id_list_count - 1

    current_index = id_list.index(obj.id)
    previous_index = 0
    next_index = last_id_index
    previous_obj_id = None
    previous_obj = None
    next_obj_id = None
    next_obj = None

    if current_index > 0:
        previous_index = current_index - 1
        previous_obj_id = id_list[previous_index]
        previous_obj = model.objects.get(pk=previous_obj_id)

    if current_index < last_id_index:
        next_index = current_index + 1
        next_obj_id = id_list[next_index]
        next_obj = model.objects.get(pk=next_obj_id)

    return [current_index, previous_obj_id, previous_obj, last_id_index, next_obj_id, next_obj]

# 专题分类
def subject(request, subject_id):
    try:
        subject_obj = Subject.objects.get(pk=subject_id)
        special_news = published_subject_news.filter(news_category__id=subject_id)
        pagination_special_news = get_page(request, special_news)

        return render(request, 'subject_list.html', locals())
    except Exception as e:
        logger.error(e)
        return render(request, 'index.html', locals())

# 专题分类文章
def special(request, special_new_id):
    try:
        special_new_obj = SpecialNews.objects.get(pk=special_new_id)

        """
            同一类别，按照发布时间的顺序得到当前文章，上一篇文章，下一篇文章
        """
        category_all_special_new_id = [subject_new.id for subject_new in published_subject_news.filter(news_category__id=special_new_obj.news_category.id)]
        values = assistant(request, special_new_obj, category_all_special_new_id, SpecialNews)

        current_special_new_index = values[0]
        previous_special_new_id = values[1]
        previous_special_new_obj = values[2]
        last_special_new_id_index = values[3]
        next_special_new_id = values[4]
        next_special_new_obj = values[5]

        special_new_obj.view_count += 1
        special_new_obj.save()

        return render(request, 'subject.html', locals())

    except Exception as e:
        logger.error(e)
        return render(request, 'index.html', locals())

# 公告通知显示页面
def notification(request, notice_id):
    try:
        notification_obj = published_notifications.get(pk=notice_id)
        notification_id_list = [note.id for note in published_notifications]

        values = assistant(request, notification_obj, notification_id_list, Notification)
        current_index = values[0]
        previous_id = values[1]
        previous_notification_obj = values[2]
        last_id_index = values[3]
        next_id = values[4]
        next_notification_obj = values[5]

        notification_obj.view_count += 1
        notification_obj.save()
        return render(request, 'notification.html', locals())
    except Exception as e:
        logger.error(e)
        return render(request, 'index.html', locals())

# 新闻new
def new(request, new_id):
    try:
        new_obj = published_articles.get(pk=new_id)

        """
            同一类别，按照发布时间的顺序得到当前文章，上一篇文章，下一篇文章
        """
        category_all_new_id = [article.id for article in published_articles.filter(news_category__id=new_obj.news_category.id)]
        values = assistant(request, new_obj, category_all_new_id, Article)

        current_article_index = values[0]
        previous_article_id = values[1]
        previous_new_obj = values[2]
        last_new_id_index = values[3]
        next_article_id = values[4]
        next_new_obj = values[5]

        new_obj.view_count += 1
        new_obj.save()

        return render(request, 'new.html', locals())
    except Exception as e:
        logger.error(e)
        return render(request, 'index.html', locals())

# 研究中心分类
def research(request, research_classfication_id):
    try:
        research_classfication_obj = research_classfications.get(pk=research_classfication_id)
        researches = published_researches.filter(news_category__id=research_classfication_id)
        pagination_researches = get_page(request, researches)
        research_center_profile_obj = research_center_profiles.get(research_classfication__id=research_classfication_id)

        return render(request, 'research_list.html', locals())
    except Exception as e:
        logger.error(e)
        return render(request, 'index.html', locals())

# 研究中心简介
def profile(request, research_center_profile_id):
    try:
        research_center_profile = research_center_profiles.get(pk=research_center_profile_id)
        return render(request, 'research_center_profile.html', locals())
    except Exception as e:
        logger.error(e)
        return render(request, 'index.html', locals())

# 具体的研究中心文章
def data(request, research_id):
    try:
        research_obj = published_researches.get(pk=research_id)

        """
            同一类别，按照发布时间的顺序得到当前文章，上一篇文章，下一篇文章
        """
        category_all_research_id = [published_research.id for published_research in published_researches.filter(news_category__id=research_obj.news_category.id)]
        values = assistant(request, research_obj, category_all_research_id, Research)

        current_research_index = values[0]
        previous_research_id = values[1]
        previous_research_obj = values[2]
        last_research_id_index = values[3]
        next_research_id = values[4]
        next_research_obj = values[5]

        research_obj.view_count += 1
        research_obj.save()

        return render(request, 'research.html', locals())
    except Exception as e:
        logger.error(e)
        return render(request, 'index.html', locals())

# 点击小分类框的设置
def category(request, category_id):
    try:
        category_obj = Category.objects.get(pk=category_id)
        category_name = category_obj.name

        if category_name == u'学院简介':
            # 学院简介
            return redirect('/introduce/')
        elif category_obj.navigation_category.name == u'学院概况':
            # 学院概况下面的除了学院简介的其他分类
            college_profile = CollegeProfile.objects.get(title=category_name)
            return render(request, 'college_profile.html', locals())
        elif category_name == u'网络教育平台':
            return redirect('http://gs.gwypx.com.cn:84/login.jsp')
        elif category_name == u'非公经济网络教育平台':
            return redirect('http://gsfg.gwypx.com.cn:84/login.jsp')
        elif category_name == u'学习秘书':
            return redirect('http://ta11.gwypx.com.cn:84/portal/login.action')
        elif category_name == u'数字图书馆':
            return redirect('http://www.zysylib.org.cn/portal/index.jsp')
        else:
            # 其他导航栏下面的子分类
            news = published_articles.filter(news_category__id=category_id)
            news = get_page(request, news)
            news.nav = category_obj.navigation_category #将小分类所对应的导航分类赋值给nav属性

            news.cate_name = category_name
            return render(request, 'new_list.html', locals())
    except Exception as e:
        logger(e)
        return render(request, 'index.html', locals())

# 最新文章
def latest_news(request):
    try:
        latest_news_list = [article for article in published_articles if is_latest_article(request, article.date_published)]
        latest_news_list = get_page(request, latest_news_list)
        return render(request, 'latest_news_list.html', locals())
    except Exception as e:
        logger.error(e)
        return render(request, 'index.html', locals())

# 下载
def download(request, value, grade, id):
    obj = None
    file_path = None
    file_name = None

    """
        注意上传的文件名不能包含中文
    """
    try:
        if value == 'notice':
            obj = published_notifications.get(pk=id)
        elif value == 'article':
            obj = published_articles.get(pk=id)
        elif value == 'subject':
            obj = published_subject_news.get(pk=id)
        else:
            obj = published_researches.get(pk=id)

        if grade == 'a':
            file_path = 'uploads/' + str(obj.download_file1)
            file_name = file_path.split('/')[-1]
        elif grade == 'b':
            file_path = 'uploads/' + str(obj.download_file2)
            file_name = file_path.split('/')[-1]
        else:
            file_path = 'uploads/' + str(obj.download_file3)
            file_name = file_path.split('/')[-1]

        def file_iterator(path, chunk_size=512): #大文件下载，设定缓存大小
            with open(path, 'rb') as rf:
                while True:
                    content = rf.read(chunk_size)
                    if content:
                        yield content
                    else:
                        break

        response = StreamingHttpResponse(file_iterator(file_path))

        #设定文件头，这种设定可以让任意文件都能正确下载，而且已知文本文件不是本地打开
        response['Content-Type'] = 'application/octet-stream'
        #设定传输给客户端的文件名称
        response['Content-Disposition'] = 'attachment; filename="{0}"'.format(file_name.encode('utf-8'))
        #传输给客户端的文件大小
        response['Content-Length'] = os.path.getsize(file_path)

        return response

    except Exception as e:
        logger.error(e)
        return render(request, 'index.html', locals())


# # 400异常处理
# def my_custom_page_bad_request_view(request):
#     return HttpResponseBadRequest('<h3>对不起,这是个无效的请求...</h3>')
#
# # 403异常处理
# def my_custom_page_forbidden_view(request):
#     return HttpResponseForbidden('<h3>对不起,访问请求拒绝...</h3>')
#
# # 404异常处理
# def my_custom_page_not_found_view(request):
#     return HttpResponseNotFound('<h3>对不起,您访问的页面没有找到...</h3>')
#
# # 500异常处理
# def my_custom_page_server_error_view(request):
#     return HttpResponseServerError('<h3>对不起,服务器发生异常错误...</h3>')
