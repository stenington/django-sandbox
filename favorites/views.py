from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Favorite

class FavoritesView(ListView):
    model = Favorite
    template_name = "favorites/favorites.html"    
    
favorites = FavoritesView.as_view()
