from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserForm
import requests
from requests.exceptions import HTTPError


class RegisterView(CreateView):
    form_class = UserForm
    template_name = 'pages-register.html'
    success_url = reverse_lazy('login')