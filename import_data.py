# import_data.py
import os
import django
import pandas as pd

# Настройка окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_project.settings')
django.setup()

from recipes.models import Recipe

def import_from_excel(file_path):
    # Читаем Excel файл. Убедитесь, что названия колонок в файле
    # соответствуют 'Название', 'Описание' и т.д.
    df = pd.read_excel(file_path)

    for index, row in df.iterrows():
        Recipe.objects.create(
            title=row['Название'],
            description=row['Описание'],
            ingredients=row['Ингредиенты'],
            instructions=row['Инструкции'],
            cooking_time=row['Время приготовления']
        )
    print("Данные успешно импортированы!")

if __name__ == "__main__":
    # Укажите путь к вашему файлу
    import_from_excel('/home/dgtr/Документы/python_projects/RecipeSite/РК.xlsx')