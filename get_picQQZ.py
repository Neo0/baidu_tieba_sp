# -*- coding: utf-8 -*-

url = 'http://tieba.baidu.com/p/2970106602'

neo_headers = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
		,'Mozilla/5.0 (Linux; U; Android 4.1.2; zh-tw; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
		,'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'
		,'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)'
		,'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36']

import urllib
import urllib2
from random import choice
import re

header = choice(neo_headers)

def get_content(url):
	html = urllib2.urlopen(url)
	content = html.read()
	html.close()
	return content

def get_picQQzone(content):
	"""
<img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=a97e769d9045d688a302b2ac94c37dab/
36fb513d269759ee57eedf65b0fb43166c22dfe7.jpg" pic_ext="jpeg" pic_type="0" width="560" height="466" 
style="cursor: url(http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur), pointer;">
	"""
	regex = r'class="BDE_Image" src="(.+?\.jpg)"'
	pat = re.compile(regex)
	images_code = re.findall(pat,content)

	count = 1

	for image_url in images_code:
		print image_url
		urllib.urlretrieve(image_url,'%s.jpg' % count)
		count += 1

content = get_content(url)
print get_picQQzone(content)