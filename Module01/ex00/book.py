class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list
        # "starter", "lunch", "dessert"
    
    def __str__(self):
        return f"{self.name} ({self.last_update})"