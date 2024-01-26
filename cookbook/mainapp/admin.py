from django.contrib import admin
from .models import *


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'amount_used']
    list_display_links = ['id', 'title', 'amount_used']


@admin.register(DishRecipe)
class DishRecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'gram_weight', 'dish_id', 'ingredient_id']
    list_display_links = ['id', 'gram_weight', 'dish_id', 'ingredient_id']
