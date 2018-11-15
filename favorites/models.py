from django.db import models

class Favorite(models.Model):
    name = models.CharField(max_length=20)
