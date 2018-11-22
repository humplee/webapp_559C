# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url,include
import os
from .views import (
    HomePageView,
    BackendEChartsTemplate,
    DefaultTopicsView,
    MaynardTemplate,
    HectorTemplate,
    GolokTemplate,
    PingTemplate,
    DavidTemplate,
    MikeTemplate,
    FredTemplate,
    AngelaTemplate,
    SatieTemplate,
    KenTemplate,
    KennyTemplate,
    ShaunaTemplate,
    JohnTemplate,
    WaiTemplate
)

urlpatterns = [
    url(r"^$", HomePageView.as_view(), name="home"),
    url(r"^Maynard$", MaynardTemplate.as_view(), name="Maynard"),
    url(r"^Hector$", HectorTemplate.as_view(), name="Hector"),
    url(r"^Golok$", GolokTemplate.as_view(), name="Golok"),
    url(r"^Ping$", PingTemplate.as_view(), name="Ping"),
    url(r"^David$", DavidTemplate.as_view(), name="David"),
    url(r"^Mike$", MikeTemplate.as_view(), name="Mike"),
    url(r"^Fred$", FredTemplate.as_view(), name="Fred"),
    url(r"^Angel$", AngelaTemplate.as_view(), name="Angel"),
    url(r"^Satie$", SatieTemplate.as_view(), name="Satie"),
    url(r"^Ken$", KenTemplate.as_view(), name="Ken"),
    url(r"^Kenny$", KennyTemplate.as_view(), name="Kenny"),
    url(r"^Shauna$", ShaunaTemplate.as_view(), name="Shauna"),
    url(r"^John$", JohnTemplate.as_view(), name="John"),
    url(r"^Wai$", WaiTemplate.as_view(), name="Wai"),
   

    #url(r'^people/(?P<twitter_id>\w+)/$',  BackendEChartsTemplate.as_view(),name="backend_charts_temp"),
    url(r"^topics$", DefaultTopicsView.as_view(), name="topics"),
    url(r"^backend_charts$", BackendEChartsTemplate.as_view(), name="backend_charts"),
]
STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\', '/')