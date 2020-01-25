from django.shortcuts import render
from django.views import generic
from .models import Recipe as RecipeModel
from django.contrib.auth.decorators import login_required

# Create your views here.


class RecipeList(generic.ListView):
    queryset = RecipeModel.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
class RecipeDetail(generic.DetailView):
    model = RecipeModel
    template_name = 'recipe_detail.html'

