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
SOCIAL = (
        ('Github', 'http://github.com/seisman'),
        ('Email', 'mailto:seisman.info@gmail.com'),
		('Weibo', 'http://weibo.com/seisman'),
		('RSS', SITEURL + "/" + FEED_ALL_RSS),
)
