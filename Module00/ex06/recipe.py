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


def printAll():
    for key, info in cookbook.items():
        print(key)
        print(f"Ingredients: {', '.join(info['ingredients'])}")
        print(f"Meal: {info['meal']}")
        print(f"Prep time: {info['prep_time']} minutes")
        print("------------------------")


def add():
    print("add")


def delete():
    print("delete")


def printRecepie():
    print("printRecepie")


if __name__ == "__main__":
    printAll()
    add()
    delete()
    printRecepie()
