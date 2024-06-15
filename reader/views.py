from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView


class IndexView(generic.TemplateView):
    template_name = "index.html"

class TopView(generic.TemplateView):
    template_name = 'index.html'