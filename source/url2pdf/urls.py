#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
#
# Created at 04.09.2020.
# Python 3.7.3 x64
# Contacts: alexandrsokolov@cock.li
#
from django import urls

from .views import IndexPage
from .views import DownloadPage

app_name = "url2pdf"

urlpatterns = [
    urls.path('u/<path:url>/', DownloadPage.as_view(), name="upload"),
    urls.path('', IndexPage.as_view(), name="index")
]
