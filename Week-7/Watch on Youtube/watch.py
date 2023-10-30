import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    x = s.split('"')
    if len(x) <2:
        return 'None'
    urlx = ''
    for i in x:
        if 'https' in i or 'http' in i:
            urlx = i
            break

    if matches := re.search(r'^https?://(www.)?youtube.com/embed/(\w+)$',urlx):
        addon = matches.group(2)
        return f'https://youtu.be/{addon}'

    else:
        return 'None'





if __name__ == "__main__":
    main()