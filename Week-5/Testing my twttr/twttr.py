def main():
    print(shorten('h,llo'))


def shorten(word):
    str = ''
    for c in word:
        if c.lower() == 'a' or c.lower() == 'e' or c.lower() == 'i' or c.lower() == 'o' or c.lower() == 'u' or c == ',' or c == '.' or c.isnumeric() == True:
            continue
        else:
            str += c
    return str


if __name__ == "__main__":
    main()