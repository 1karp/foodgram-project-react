from django.contrib import admin

from .models import Ingredient, Recipe, Tag, Cart, Favorites


admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(Recipe)
admin.site.register(Cart)
admin.site.register(Favorites)
