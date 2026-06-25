Rtype = ("starter", "lunch", "dessert")


class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 description, recipe_type):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        if not isinstance(cooking_lvl, int):
            raise ValueError("lvl must be int")
        if cooking_lvl < 1 or cooking_lvl > 5:
            raise ValueError("lvl must be between 1 and 5")
        if not isinstance(cooking_time, int):
            raise ValueError("time must be int")
        if cooking_time < 0:
            raise ValueError("cooking_time cannot be negative")
        if not isinstance(ingredients, list) or len(ingredients) == 0:
            raise ValueError("ingredients must be a non-empty list")
        for item in ingredients:
            if not isinstance(item, str):
                raise ValueError("all ingredients must be strings")
        if not isinstance(description, str):
            raise ValueError("description must be a string")
        if recipe_type not in Rtype:
            raise ValueError("Recipe type must be starter, lunch or dessert")
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.cooking_lvl = cooking_lvl
        self.recipe_type = recipe_type

    def __str__(self):
        ingredients = ", ".join(self.ingredients)
        desc = self.description if self.description else "No description"
        return (
            f"Name: {self.name}\n"
            f"Level: {self.cooking_lvl}/5\n"
            f"Cooking time: {self.cooking_time} minutes\n"
            f"Ingredients: {ingredients}\n"
            f"Description: {desc}\n"
            f"Type: {self.recipe_type}"
        )
