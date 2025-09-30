# recipes/models.py
from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200) # Название рецепта
    description = models.TextField() # Краткое описание
    ingredients = models.TextField() # Ингредиенты (пока просто текстом)
    instructions = models.TextField() # Инструкции по приготовлению
    cooking_time = models.IntegerField() # Время приготовления в минутах
    # Можно добавить и другие поля: калории, фото и т.д.
    # image = models.ImageField(upload_to='recipes/')

    def __str__(self):
        return self.title