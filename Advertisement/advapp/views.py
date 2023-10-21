from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Advertisement, Response
from .forms import AdvForm, ResponseForm


class AdvList(ListView):
    model = Advertisement
    ordering = '-date'
    template_name = 'adv_list.html'
    context_object_name = 'advertisements'
    paginate_by = 3


class AdvDetail(DetailView):
    model = Advertisement
    template_name = 'adv_detail.html'
    context_object_name = 'advertisement'
    paginate_by = 3


class AdvCreate(PermissionRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('advapp.add_advertisement',)
    form_class = AdvForm
    model = Advertisement
    template_name = 'adv_edit.html'


class AdvEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('advapp.change_advertisement',)
    form_class = AdvForm
    model = Advertisement
    template_name = 'adv_edit.html'


class AdvDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('advapp.delete_advertisement',)
    model = Advertisement
    template_name = 'adv_delete.html'
    success_url = reverse_lazy('adv_list')


class AddResponse(CreateView):
    permission_required = ('advapp.add_permission',)
    form_class = ResponseForm
    model = Response
    template_name = 'add_response.html'

