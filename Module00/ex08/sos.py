import sys

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}


def main():
    if len(sys.argv) == 1:
        print("ERROR")
        quit()
    args = sys.argv[1:]
    text = " ".join(args)
    text = text.upper()
    for c in text:
        if not (c.isalnum() or c == ' '):
            print("ERROR")
            quit()
    translation = []
    for letter in text:
        if letter == ' ':
            translation.append('/')
        else:
            translation.append(MORSE_CODE_DICT[letter])

    result = " ".join(translation)
    print(result)


if __name__ == "__main__":
    main()
