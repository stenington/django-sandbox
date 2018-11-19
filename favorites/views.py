from django.shortcuts import render
from django.views.generic.list import ListView

class FavoritesListView(ListView):
    model = Favorite
    template_name = "favorites_list.html"

