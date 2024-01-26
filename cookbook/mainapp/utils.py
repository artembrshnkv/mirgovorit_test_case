# from .models import Ingredient, DishRecipe
#
#
# def actualise_ingredient_quantity(ingredient_id):
#     ingredient = Ingredient.objects.get(pk=ingredient_id)
#
#     actual_quantity = DishRecipe.objects.filter(ingredient_id=ingredient_id).count()
#     stored_quantity = ingredient.amount_used
#
#     if actual_quantity != stored_quantity:
#         ingredient.update(amount_used=actual_quantity)
