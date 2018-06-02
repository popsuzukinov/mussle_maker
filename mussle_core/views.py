from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import *
from django.views.generic.edit import FormMixin, DeletionMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import *
from mussle_core.models import Musslemenu


class MussleList(TemplateView, ListView):
    template_name = 'mussle_list.html'
    model = Musslemenu

    def get_context_data(self, **kwargs):
        context = super(MussleList, self).get_context_data(**kwargs)
        context['mussle_lists'] = Musslemenu.objects.all()
        return context
