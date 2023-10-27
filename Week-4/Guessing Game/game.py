import random
import sys
while True:
    try:
        x = int(input('Level: '))
        if x>0:
            y = random.randint(1,x)
            while True:
                try:
                    z = int(input('Guess: '))
                    if z>0:
                        if y == z:
                            sys.exit("Just right!")
                        elif y > z:
                            print('Too small!')
                        else:
                            print('Too large!')
                except ValueError:
                    pass
    except ValueError:
        pass