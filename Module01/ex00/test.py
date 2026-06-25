from book import Book
from recipe import Recipe


def test_recipe():
    try:
        recipe = Recipe("Salad", 3, 45, ["Tomatos", "Olives"],
                        "Summer salad", "lunch")
        to_print = str(recipe)
        print(to_print)
    except ValueError as e:
        print(f"Error: {e}")


def test_book():
    try:
        book = Book("My cookbook")
        to_print = str(book)
        print(to_print)
        print("----------")
        cake = Recipe("Cake", 3, 45, ["flour", "eggs", "sugar"],
                      "Simple cake", "dessert")
        salad = Recipe("Salad", 1, 45, ["Tomatos", "Olives"],
                       "Summer salad", "lunch")
        book.add_recipe(cake)
        book.add_recipe(salad)
        found = book.get_recipes_by_types("dessert")
        if not found:
            print("No Recipes found")
        for r in found:
            to_print = str(r)
            print(to_print)
            print("----------")
        found = book.get_recipe_by_name("Salad")
        if found is None:
            print("No recipes found")
        else:
            print(found)
        print("----------")
        to_print = str(book)
        print(to_print)
    except ValueError as e:
        print(f"Error: {e}")


def main():
    test_recipe()
    print("-------------------------------")
    test_book()


if __name__ == "__main__":
    main()
