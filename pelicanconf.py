#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pat David'
SITENAME = u'GIMP'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Pat David changes while building/testing

# This will copy over these folders w/o modification
STATIC_PATHS = ['images', 'pages']


THEME = "./themes/newgimp"

# Trying to properly nest sub-folders here
#PATH_METADATA = r".*?\\(?P<test>.*?\\)" #old test

#see: https://github.com/getpelican/pelican/issues/1128#issuecomment-63251758
PATH_METADATA = r'.*?\\(?P<test>(.+\\)?).*' 

# Still working on this...
#PAGE_URL = "{test}{slug}/"
#PAGE_SAVE_AS = "{test}{slug}/index.html"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

ARTICLE_URL = "news/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "news/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

TYPOGRIFY = True
TYPOGRIFY_IGNORE_TAGS = ['title']

DELETE_OUTPUT_DIRECTORY = True