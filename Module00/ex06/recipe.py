cookbook = {
    "sandwich": {
        "ingredients": ("ham", "bread", "cheese", "tomatoes"),
        "meal": "lunch",
        "prep_time": "10"
    },
    "cake": {
        "ingredients": ("flour", "sugar", "eggs"),
        "meal": "dessert",
        "prep_time": "60"
    },
    "salad": {
        "ingredients": ("avocado", "arugula", "tomatoes", "spinach"),
        "meal": "lunch",
        "prep_time": "15"
    }
}


def printAllKeys():
    keys = list(cookbook.keys())
    for k in keys:
        print(k)


def addRecepie():
    print("Enter a name:")
    name = input(">> ")
    if name in cookbook:
        print("Recipe already exists.")
        return

    print("Enter ingredients:")
    ingredients = input(">> ").split(",")

    ingredients = tuple(i.strip() for i in ingredients)

    print("Enter a meal type:")
    meal = input(">> ")

    print("Enter a preparation time:")
    prep_time = input(">> ")

    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }
    print(f"Recipe '{name}' added successfully.")


def deleteRecepie():
    print("Please enter a recipe name to delete:")
    name = input(">> ")
    if name in cookbook:
        del cookbook[name]
        print(f"Recipe '{name}' deleted.")
    else:
        print("Recipe not found.")


def printRecepie():
    print("Please enter a recipe name to get its details:")
    name = input(">> ")
    if not name or name == "":
        printRecepie()
    else:
        try:
            resepie = cookbook[name]
            print(f"Ingredients: {', '.join(resepie['ingredients'])}")
            print(f"Meal: {resepie['meal']}")
            print(f"Prep time: {resepie['prep_time']} minutes")
        except KeyError:
            printRecepie()


def exitProg():
    print("Cookbook closed. Goodbye !")
    quit()


def info():
    print("""List of available options:
    1: Add a recipe
    2: Delete a recipe
    3: Print a recipe
    4: Print the cookbook
    5: Quit
    """)


def selectOption():
    print("Please select an option:")
    text = input(">> ")
    if not text or text == "":
        selectOption()
    else:
        try:
            val = int(text)
            if val == 1:
                addRecepie()
            elif val == 2:
                deleteRecepie()
            elif val == 3:
                printRecepie()
            elif val == 4:
                printAllKeys()
            elif val == 5:
                exitProg()
            else:
                print("Sorry, this option does not exist.")
                info()
        except ValueError:
            print("Sorry, this option does not exist.")
            info()
        selectOption()


def main():
    print("Welcome to the Python Cookbook !")
    info()
    selectOption()


if __name__ == "__main__":
    main()
