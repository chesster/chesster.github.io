#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Łukasz Malik'
SITENAME = 'Malik.pro'
SITEURL = 'https://blog.malik.pro'



TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

PATH = 'content'
THEME = 'pelicanyan'
GA_ACCOUNT = 'UA-12344321-1'
TWITTER_ACCOUNT = 'getpelican'
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'sitemap', 'robots', 'humans')
ROBOTS_SAVE_AS = 'robots.txt'
HUMANS_SAVE_AS = 'humans.txt'
SITEMAP_SAVE_AS = 'sitemap.xml'
DEFAULT_LANG = 'en'
DATE_FORMATS = { 'en': '%B %d, %Y', }
STATIC_PATHS = ['images', 'favicon.ico']
SITEDESCRIPTION = 'sample blog'
TYPOGRIFY=True

STATIC_PATHS = ['static/CNAME',]
EXTRA_PATH_METADATA = {'static/CNAME': {'path': 'CNAME'},}