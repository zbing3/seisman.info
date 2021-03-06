#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

###########################################################
##                     Basic settings                    ##
###########################################################
SITEURL = u'http://localhost:8000'
AUTHOR = u'SeisMan'
DATE_FORMATS = {
	'zh': ('zh_CN', '%x'),
	'en': ('en_US', '%a, %d %b %Y'),
}
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = '其他'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_DATE = 'fs'
# DEFAULT_DATE = (2099, 01, 01, 00, 00, 00)
DEFAULT_METADATA = ()
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
PATH_METADATA = ''
DELETE_OUTPUT_DIRECTORY = False
OUTPUT_RETENTION = ()
JINJA_EXTENSIONS = []
JINJA_FILTERS = {}
LOCALE = ('zh_CN', 'en_US')
READERS = {}
IGNORE_FILES = ['.#*']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
OUTPUT_PATH = 'output/'
PATH = None
PAGE_DIR = 'pages'
PAGE_EXCLUDES = ()
ARTICLE_DIR = ''
ARTICLE_EXCLUDES = ('pages', 'drafts')
OUTPUT_SOURCES = False
OUTPUT_SOURCES_EXTENSION = '.text'
RELATIVE_URLS = False
SITENAME = u'SeisMan'
SITEURL = ''
TEMPLATE_PAGES = None
TIMEZONE = 'Asia/Shanghai'
TYPOGRIFY = True
DIRECT_TEMPLATES = ('index', 'tags', 'categories','archives', 'search', '404')
PAGINATED_DIRECT_TEMPLATES = ('index',)
SUMMARY_MAX_LENGTH = 50
ASCIIDOC_OPTIONS = []
WITH_FUTURE_DATES = False
INTRASITE_LINK_REGEX = '[{|](?P<what>.*?)[|}]'
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

STATIC_PATHS = [
	'images',
	'theme/images',
]

EXTRA_PATH_METADATA = {}

###########################################################
##                     URL settings                      ##
###########################################################
ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_LANG_URL = '{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = ''
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = ''
TAGS_URL = 'tags'
TAGS_SAVE_AS = 'tags.html'
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = ''
AUTHORS_URL = 'authors.html'
AUTHORS_SAVE_AS = 'authors.html'
ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = False
MONTH_ARCHIVE_SAVE_AS = False
DAY_ARCHIVE_SAVE_AS = False
SLUG_SUBSTITUTIONS = ()

###########################################################
##                       Feed Settings                   ##
###########################################################
# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
#FEED_RSS = None
#FEED_ALL_RSS = 'feed/rss.xml'
#CATEGORY_FEED_RSS = 'feed/%s.rss.xml'
#TAG_FEED_RSS = None
FEED_ATOM = None
FEED_ALL_ATOM = 'feed/all.atom.xml'
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM = None
FEED_MAX_ITEMS = ''

###########################################################
##                       Pagination                      ##
###########################################################
DEFAULT_ORPHANS = 0 
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = [
	(0, '{name}{number}.html', '{name}{number}.html'),
]

###########################################################
##                         Tag Cloud                     ##
###########################################################
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

###########################################################
##                   Translations                        ##
###########################################################
DEFAULT_LANG = 'zh'
TRANSLATION_FEED_ATOM = 'feed/all-%s.atom.xml'
TRANSLATION_FEED_RSS = None

###########################################################
##                      Ordering content                 ##
###########################################################
NEWEST_FIRST_ARCHIVES = True
REVERSE_CATEGORY_ORDER = False

###########################################################
##                        Theme                          ##
###########################################################
THEME = "themes/Elegant_SeisMan"
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'main.css'

###########################################################
##                          Plugins                      ##
###########################################################
PLUGIN_PATH = 'plugins'
PLUGINS = [
	'sitemap',
	'extract_toc',
	'tipue_search',
    'latex',
    'neighbors',
    'assets',
    'related_posts',
    'multi_part'
]

###########################################################
##                       Plugin: Sitemap                 ##
###########################################################
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.5,
        'pages': 0.3
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

## Elegant Theme
RECENT_ARTICLES_COUNT = 15
COMMENTS_INTRO = u'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'
SITE_LICENSE = u'Copyright &copy; 2013-2014 <a href="http://seisman.info"><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title"> SeisMan</span></a>. All Rights Reserved.'
SITE_DESCRIPTION = u'关注和分享地震学相关知识、软件、代码。'
SITE_SUBTITLE = u'学会整理自己的经验是科研的第一步。'
USE_SHORTCUT_ICONS = True
#LANDING_PAGE_ABOUT
#PROJECTS

# MailChimp
EMAIL_SUBSCRIPTION_LABEL = u'Get Weekly Updates'
EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
MAILCHIMP_FORM_ACTION = u'http://seisman.us3.list-manage1.com/subscribe/post?u=03bdd9e889c533d6db4dd0454&amp;id=dc5a50f619'

DISQUS_SITENAME = u'seisman'

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
		'url': SITEURL + "/" + FEED_ALL_ATOM},
	{
		'icon': 'CNY',
		'title': '捐赠本博',
        'url': 'http://seisman.info/donation.html'},
]
