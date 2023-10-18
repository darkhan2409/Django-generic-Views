from django.shortcuts import render
from .models import *
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy


class CountryList(ListView):
    model = Country
    context_object_name = 'countries'
    template_name = 'country_list_template.html'


class CountryDetail(DetailView):
    model = Country
    context_object_name = 'country'
    template_name = 'country_detail_template.html'


class CountryCreate(CreateView):
    model = Country
    template_name = 'country_create_template.html'
    fields = ['title', 'description', 'capital', 'population', 'square']
    success_url = reverse_lazy('country_list_url')


class CountryUpdate(UpdateView):
    model = Country
    template_name = 'country_update_template.html'
    fields = ['title', 'description', 'capital', 'population', 'square']
    success_url = reverse_lazy('country_list_url')


class CountryDelete(DeleteView):
    model = Country
    template_name = 'country_delete_template.html'
    context_object_name = 'country'
    success_url = reverse_lazy('country_list_url')

