import random


def game(num, attempt):
    print("What's your guess between 1 and 99?")
    inp = input(">> ")
    try:
        val = int(inp)
        if val < num:
            print("Too low!")
        elif val > num:
            print("Too high!")
        else:
            print("Congratulations, you've got it!")
            print(f"You won in {attempt} attempts!")
            quit()
    except ValueError:
        print("That's not a number.")
    attempt += 1
    game(num, attempt)


def main():
    print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
    """)
    num = random.randint(1, 99)
    game(num, 1)


if __name__ == "__main__":
    main()
