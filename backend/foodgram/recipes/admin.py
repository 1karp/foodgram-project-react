from django.contrib import admin
from users.models import Follow

from .models import Ingredient, Recipe, Tag

admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(Recipe)
admin.site.register(Follow)
