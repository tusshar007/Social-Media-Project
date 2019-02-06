from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                    PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from .models import Group,GroupMember

class CreateGroup(LoginRequiredMixin,CreateView):
    fields=('name','description')
    models = Group

class SingleGroup(generic.DetailView):
    model=Group

class ListGroups(generic.ListView):
    model = Group
