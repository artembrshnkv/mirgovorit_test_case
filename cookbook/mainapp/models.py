from django.db import models


class Dish(models.Model):
    title = models.CharField(verbose_name='Блюдо', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюдо'


class Ingredient(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    amount_used = models.PositiveIntegerField(
        verbose_name='Использованно',
        null=True,
        default=0,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class DishRecipe(models.Model):
    dish = models.ForeignKey(
        verbose_name='Блюдо',
        to=Dish,
        on_delete=models.PROTECT
    )
    ingredient = models.ForeignKey(
        verbose_name='Ингридиент',
        to=Ingredient,
        on_delete=models.PROTECT
    )
    gram_weight = models.PositiveIntegerField(verbose_name='Вес в граммах')

    def save(self, *args, **kwargs):
        ingredient_id = Ingredient.objects.get(title=self.ingredient).pk

        actual_quantity = DishRecipe.objects.filter(ingredient_id=ingredient_id).count()
        stored_quantity = Ingredient.objects.get(pk=ingredient_id).amount_used

        if actual_quantity != stored_quantity or stored_quantity == 0:
            Ingredient.objects.filter(pk=ingredient_id).update(amount_used=actual_quantity)

        print(self.ingredient)
        print(ingredient_id)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Рецепт блюда'
        verbose_name_plural = 'Рецепты блюд'
        constraints = [
            models.UniqueConstraint(
                name='unique_ingredient_for_dish',
                fields=['dish', 'ingredient']
            )
        ]
