from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F

from .models import DishRecipe, Ingredient, Dish


def add_product_to_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET['recipe_id']
        product_id = request.GET['product_id']
        weight = request.GET['weight']

        if recipe_id and product_id and weight:
            DishRecipe.objects.update_or_create(
                pk=recipe_id,
                ingredient_id=product_id,
                defaults={'gram_weight': weight},
                create_defaults={
                    'pk': recipe_id,
                    'ingredient_id': product_id,
                    'gram_weight': weight
                }
            )

    return HttpResponse('')


def cook_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET['recipe_id']

        dish_ingredients = DishRecipe.objects.filter(dish_id=recipe_id).\
            values_list('ingredient_id')
        used_ingredients_ids = [i[0] for i in dish_ingredients]

        if used_ingredients_ids:
            Ingredient.objects.filter(pk__in=used_ingredients_ids).\
                update(amount_used=F('amount_used') + 1)

    return HttpResponse('')


def show_recipes_without_product(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']

        dishes_with_stated_ingredient = DishRecipe.objects. \
            filter(ingredient_id=product_id, gram_weight__gte=10)

        matching_dishes = Dish.objects.\
            filter(~Q(pk__in=dishes_with_stated_ingredient)).\
            values_list('pk')

        recipes_for_template = []
        for dish in matching_dishes:
            ingredients = DishRecipe.objects.\
                filter(dish_id=dish[0]).\
                values_list('ingredient__title')
            recipe = {
                'dish_id': dish[0],
                'ingredients': [i[0] for i in ingredients]
            }
            recipes_for_template.append(recipe)

    return render(
        request,
        'mainapp/show_recipes_without_products.html',
        {'recipes': recipes_for_template}
    )
