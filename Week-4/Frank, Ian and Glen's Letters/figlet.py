import sys
import random
import pyfiglet

font_list = [
    "banner",
    "big",
    "block",
    "bubble",
    "doom",
    "lean",
    "mini",
    "poison",
    "script",
    "shadow",
    "slant",
    "small",
    "standard",
    "starwars",
    "rectangles",
    "alphabet"
]



if len(sys.argv) == 1:
    str = input('Input: ')
    n = len(font_list)
    i =random.randint(1,n) -1
    f = pyfiglet.Figlet(font = font_list[i])
    print('Output',f.renderText(str))
    sys.exit()

elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        try:
            index = font_list.index(sys.argv[2])
            str = input('Input: ')
            f = pyfiglet.Figlet(font = font_list[index])
            print(f'Output: {f.renderText(str)}')
            sys.exit()
        except ValueError:
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')
else:
    sys.exit('Invalid usage')





