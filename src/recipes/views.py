from django.shortcuts import render  # imported by default
# to display lists and details
from django.views.generic import ListView, DetailView
from .models import Recipe  # to access Recipe model

# Create your views here.


def home(request):
    return render(request, 'recipes/recipes_home.html')

# Create your views here.


class RecipeListView(ListView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/main.html'  # specify template


class RecipeDetailView(DetailView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/detail.html'  # specify template
