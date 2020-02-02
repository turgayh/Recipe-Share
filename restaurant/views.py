from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe as RecipeModel
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


class RecipeList(generic.ListView):
    queryset = RecipeModel.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class RecipeDetail(generic.DetailView):
    model = RecipeModel
    template_name = 'recipe_detail.html'


class RecipeUpdate(generic.UpdateView):
    model = RecipeModel
    fields = ['name']
    template_name = 'edit.html'
