from django.shortcuts import render  # imported by default
# to display lists and details
from django.views.generic import ListView, DetailView
from .models import Recipe  # to access Recipe model
# to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
# to protect function-based views
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request, 'recipes/recipes_home.html')


class RecipeListView(LoginRequiredMixin, ListView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/main.html'  # specify template


class RecipeDetailView(LoginRequiredMixin, DetailView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/detail.html'  # specify template

# define function-based view - records(records()

# keep protected


@login_required
def records(request):
    # do nothing, simply display page
    return render(request, 'recipes/records.html')
