import sys
import string


def filter(s, n):
    table = str.maketrans("", "", string.punctuation)
    # str.maketrans(x, y, z)
    # x - Какие символы заменять.
    # y - На что заменять.
    # z - Какие символы удалить.
    clean = s.translate(table)
    words = clean.split()
    result = [word for word in words if len(word) > n]
    print(result)


def main():
    if len(sys.argv) != 3:
        print("ERROR")
        quit()
    try:
        s = sys.argv[1]
        n = int(sys.argv[2])
        filter(s, n)
    except ValueError:
        print("ERROR")


if __name__ == "__main__":
    main()
