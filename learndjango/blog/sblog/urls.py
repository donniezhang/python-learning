#!/usr/bin/env python
#-*- coding: utf-8 -*-

from django.conf.urls import *
from sblog.views import *

urlpatterns = patterns(('sblog.views'),
		url(r'^bloglist/$','blog_list', name='bloglist'),
)
