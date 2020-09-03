#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
#
# Created at 02.09.2020.
# Python 3.7.3 x64
# Contacts: alexandrsokolov@cock.li
#
from django import urls

from .views import IndexPage
from .views import ViewPage

app_name = "dropnote"

urlpatterns = [
    urls.path('', IndexPage.as_view(), name="index"),
    urls.path('<str:pk>/', ViewPage.as_view(), name="view"),
]
