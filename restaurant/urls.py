from django.contrib import admin
from django.urls import path
from restaurant import views


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path(r'^(?P<id>\d+)/edit/$', views.RecipeUpdate.as_view(), name='edit'),
]
