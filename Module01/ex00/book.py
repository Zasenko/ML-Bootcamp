from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Book name must be a non-empty string")
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }

    def __str__(self):
        total = sum(len(recipes) for recipes in self.recipes_list.values())
        text = f"{self.name} (last_update: {self.last_update}, "
        f"creation_date: {self.creation_date}, recipes count: {total})"
        return text

    def get_recipe_by_name(self, name):
        for recipes in self.recipes_list.values():
            for r in recipes:
                if r.name == name:
                    return r
        return None

    def get_recipes_by_types(self, recipe_type):
        if recipe_type not in self.recipes_list:
            raise ValueError("Invalid recipe type")
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            raise TypeError("recipe must be a Recipe instance")
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
