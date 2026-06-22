import string
import sys


def analyze(text):
    printable = sum(1 for i in text if i.isprintable())
    upper = sum(1 for i in text if i.isupper())
    lower = sum(1 for i in text if i.islower())
    punctuation = sum(1 for i in text if i in string.punctuation)
    spaces = sum(1 for i in text if i.isspace())
    print(f"The text contains {printable} printable character(s):")
    print(f"- {upper} upper letter(s)")
    print(f"- {lower} lower letter(s)")
    print(f"- {punctuation} punctuation mark(s)")
    print(f"- {spaces} space(s)")
    print("------------------")


def text_analyzer(text=None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if not text:
        print("What is the text to analyze?")
        text = input(">> ")
        text_analyzer(text)
    elif not isinstance(text, str):
        print("AssertionError: argument is not a string")
    else:
        analyze(text)


def main():
    count = len(sys.argv)
    if count != 2:
        print("AssertionError: more than 1 argument")
    else:
        text_analyzer(sys.argv[1])


if __name__ == "__main__":
    main()
