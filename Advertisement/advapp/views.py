from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy, reverse
from .models import Advertisement, Response
from .forms import AdvForm, ResponseForm


class AdvList(ListView):
    model = Advertisement
    ordering = '-date'
    template_name = 'adv_list.html'
    context_object_name = 'advertisements'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class AdvDetail(DetailView):
    model = Advertisement
    template_name = 'adv_detail.html'
    context_object_name = 'advertisement'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = Response.objects.filter(advertisement=self.kwargs['pk'])
        context['response'] = response
        return context


class AdvCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = AdvForm
    model = Advertisement
    template_name = 'adv_edit.html'
    success_url = reverse_lazy('adv_list')

    def form_valid(self, form):
        advertisement = form.save(commit=False)
        advertisement.author = self.request.user
        advertisement.save()
        return super().form_valid(form)


class AdvEdit(LoginRequiredMixin, UpdateView):
    form_class = AdvForm
    model = Advertisement
    template_name = 'adv_edit.html'


class AdvDelete(LoginRequiredMixin, DeleteView):
    model = Advertisement
    template_name = 'adv_delete.html'
    success_url = reverse_lazy('adv_list')


class AddResponse(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = ResponseForm
    model = Response
    template_name = 'add_response.html'
    success_url = reverse_lazy('adv_list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        user = request.user
        advertisement = Advertisement.objects.get(pk=kwargs['pk'])
        if form.is_valid():
            response = form.save(commit=False)
            response.author = user
            response.advertisement = advertisement
            response.save()
            return self.form_valid(form)

        return reverse('adv_list', args=[str(self.pk)])


class ResponseList(ListView):
    model = Response
    ordering = '-date'
    template_name = 'resp_list.html'
    context_object_name = 'responses'

    def get_queryset(self):
        return Response.objects.filter(advertisement__author=self.request.user)


class ResponseDetail(DetailView):
    model = Response
    template_name = 'resp_detail.html'
    context_object_name = 'response'


class Profile(LoginRequiredMixin, ListView):
    model = Advertisement
    ordering = '-date'
    template_name = 'profile.html'
    context_object_name = 'profile'
    paginate_by = 3

    def get_queryset(self):
        return Advertisement.objects.filter(author=self.request.user)


class RespDelete(LoginRequiredMixin, DeleteView):
    model = Response
    template_name = 'resp_delete.html'
    success_url = reverse_lazy('responses')


def response_good(request, response, advertisement):
    response = get_object_or_404(Response, id=response)
    response.status = True
    response.save()
    return redirect('adv_detail', pk=advertisement)


def response_bad(request, response, advertisement):
    response = get_object_or_404(Response, id=response)
    response.status = False
    response.save()
    return redirect('adv_detail', pk=advertisement)

