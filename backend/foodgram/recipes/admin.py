from django.contrib import admin

from .models import Cart, Favorites, Ingredient, Recipe, Tag, RecipeIngredient


class IngredientAdmin(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientAdmin,
    ]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(Cart)
admin.site.register(Favorites)
