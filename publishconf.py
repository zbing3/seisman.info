#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://seisman.github.io'
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

## Social
SOCIAL = [
	{	
		'icon': 'GitHub',
		'title': 'GitHub主页',
		'url':  'http://github.com/seisman'},
	{	
		'icon': 'envelope',
		'title': '电子邮件',
		'url': 'mailto:seisman.info@gmail.com'},
	{	
		'icon': 'Weibo',
		'title': '新浪微博',
		'url': 'http://weibo.com/seisman'},
	{
		'icon': 'RSS',
		'title': 'RSS订阅',
		'url': SITEURL + "/" + FEED_ALL_RSS},
	{
		'icon': 'CNY',
		'title': '捐助本站',
		'url': 'http://me.alipay.com/seisman'},
]
