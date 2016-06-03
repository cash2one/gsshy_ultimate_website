
# 链接导航列表，包含主要媒体、统战系统、各省社院、市州社院
links = Link.objects.all()

links_list = list()

meiti_links = links.filter(link_category__name=u'主要媒体')
meiti_links.index = 1
meiti_links.display = 1
meiti_links.id = links.get(name=u'主要媒体').id
links_list.append(meiti_links)

tongzhan_links = links.filter(link_category__name=u'统战系统')
tongzhan_links.index = 2
tongzhan_links.display = 0
tongzhan_links.id = links.get(name=u'统战系统').id
links_list.append(tongzhan_links)

gesheng_links = links.filter(link_category__name=u'各省社院')
gesheng_links.index = 3
gesheng_links.display = 0
gesheng_links.id = links.get(name=u'各省社院').id
links_list.append(gesheng_links)

shizhou_links = links.filter(link_category__name=u'市州社院')
shizhou_links.index = 4
shizhou_links.display = 0
shizhou_links.id = links.get(name=u'市州社院').id
links_list.append(shizhou_links)