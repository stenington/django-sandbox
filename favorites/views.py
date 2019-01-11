from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Favorite
from django.views.generic.edit import CreateView

class FavoritesView(ListView):
    model = Favorite
    template_name = "favorites/favorites.html"    
    
favorites = FavoritesView.as_view()

class NewFavoriteView(CreateView):
    model = Favorite
    fields = ['name']
    template_name = "favorites/new-favorite.html"
    success_url = '/'

new_favorite = NewFavoriteView.as_view()
