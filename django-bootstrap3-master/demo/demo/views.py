# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

from pyecharts import Bar
from django_echarts.views.backend import EChartsBackendView

# http://yuji.wordpress.com/2013/01/30/django-form-field-in-initial-data-requires-a-fieldfile-instance/
class FakeField(object):
    storage = default_storage


fieldfile = FieldFile(None, FakeField, "dummy.txt")


class HomePageView(TemplateView):
    template_name = "demo/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        
        return context





class PaginationView(TemplateView):
    template_name = "demo/pagination.html"

    def get_context_data(self, **kwargs):
        context = super(PaginationView, self).get_context_data(**kwargs)
        lines = []
        for i in range(200):
            lines.append("Line %s" % (i + 1))
        paginator = Paginator(lines, 11)
        page = self.request.GET.get("page")
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_lines = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            show_lines = paginator.page(paginator.num_pages)
        context["lines"] = show_lines
        return context
        
        
class BackendEChartsTemplate(EChartsBackendView): 
    template_name = 'demo/backend_charts.html'
    def get_echarts_instance(self, *args, **kwargs):
        
        return
class MaynardTemplate(EChartsBackendView): 
    template_name = 'demo/Maynard.html'
    def get_echarts_instance(self, *args, **kwargs):
        
        return
class HectorTemplate(EChartsBackendView): 
    template_name = 'demo/Hector.html'
    def get_echarts_instance(self, *args, **kwargs):
        
        return
class GolokTemplate(EChartsBackendView): 
    template_name = 'demo/Golok.html'
    def get_echarts_instance(self, *args, **kwargs):
        
        return
    
class PingTemplate(EChartsBackendView): 
    template_name = 'demo/Ping.html'
    def get_echarts_instance(self, *args, **kwargs):
        
        return
class DavidTemplate(EChartsBackendView): 
    template_name = 'demo/David.html'
    def get_echarts_instance(self, *args, **kwargs):
        
        return    
class MikeTemplate(EChartsBackendView): 
    template_name = 'demo/Mike.html'
    def get_echarts_instance(self, *args, **kwargs):
        
        return
class FredTemplate(EChartsBackendView): 
    template_name = 'demo/Fred.html'
    def get_echarts_instance(self, *args, **kwargs):
        
        return
class AngelaTemplate(EChartsBackendView): 
    template_name = 'demo/Angela.html'
    def get_echarts_instance(self, *args, **kwargs):
        
        return
class SatieTemplate(EChartsBackendView): 
    template_name = 'demo/Satie.html'
    def get_echarts_instance(self, *args, **kwargs):
        
        return
class KenTemplate(EChartsBackendView): 
    template_name = 'demo/Ken.html'
    def get_echarts_instance(self, *args, **kwargs):
        
        return
class KennyTemplate(EChartsBackendView): 
    template_name = 'demo/Kenny.html'
    def get_echarts_instance(self, *args, **kwargs):
        
        return
class ShaunaTemplate(EChartsBackendView): 
    template_name = 'demo/Shauna.html'
    def get_echarts_instance(self, *args, **kwargs):
        
        return
class JohnTemplate(EChartsBackendView): 
    template_name = 'demo/John.html'
    def get_echarts_instance(self, *args, **kwargs):
        
        return
class WaiTemplate(EChartsBackendView): 
    template_name = 'demo/Wai.html'
    def get_echarts_instance(self, *args, **kwargs):
        
        return









class DefaultTopicsView(EChartsBackendView):
    template_name = "demo/topics.html"
    def get_echarts_instance(self, *args, **kwargs):
        
        return
