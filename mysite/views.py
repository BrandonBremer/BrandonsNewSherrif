# mysite/views.py

from django.shortcuts import render
from django.urls import reverse_lazy


class Login_Error(View):
    template_name = 'login_error.html'