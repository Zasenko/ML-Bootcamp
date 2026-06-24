class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type


    def __str__(self):
        return f"{self.name} ({self.cooking_lvl})"
    

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        #... Your code here ...


    def get_recipes_by_types(self, recipe_type):
        """Gets all recipes names for a given recipe_type """
        #... Your code here ...


    def add_recipe(self, recipe):
        """Adds a recipe to the book and updates last_update"""
