import sys

c = len(sys.argv)
text = ""
if (c > 1):
    i = 1
    while (i < c):
        text += sys.argv[i]
        if (i != c - 1):
            text += " "
        i += 1
    text = text[::-1]
    text = text.swapcase()
    print(text)
