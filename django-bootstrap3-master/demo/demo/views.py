# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

from .forms import ContactForm, FilesForm, ContactFormSet
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


class DefaultFormsetView(FormView):
    template_name = "demo/formset.html"
    form_class = ContactFormSet

class DefaultTopicsView(FormView):
    template_name = "demo/topics.html"
    form_class = ContactFormSet

class DefaultFormView(FormView):
    template_name = "demo/form.html"
    form_class = ContactForm


class DefaultFormByFieldView(FormView):
    template_name = "demo/form_by_field.html"
    form_class = ContactForm


class FormHorizontalView(FormView):
    template_name = "demo/form_horizontal.html"
    form_class = ContactForm


class FormInlineView(FormView):
    template_name = "demo/form_inline.html"
    form_class = ContactForm


class FormWithFilesView(FormView):
    template_name = "demo/form_with_files.html"
    form_class = FilesForm

    def get_context_data(self, **kwargs):
        context = super(FormWithFilesView, self).get_context_data(**kwargs)
        context["layout"] = self.request.GET.get("layout", "vertical")
        return context

    def get_initial(self):
        return {"file4": fieldfile}


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
        bar = Bar("我的第一个图表", "这里是副标题")
        bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
        return bar

class MiscView(TemplateView):
    template_name = "demo/misc.html"
