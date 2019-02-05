from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
# Create your views here.
from django.views.generic import CreateView
from . import forms

class Signup(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
