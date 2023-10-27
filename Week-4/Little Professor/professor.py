import random


def main():
    x = get_level()
    j = 0
    score = 0
    while j<10:
        nums = generate_integer(x)
        i = 0
        while i<3:
            try:
                z = int(input(f'{nums[0]} + {nums[1]} = '))
                if z == nums[0] + nums[1]:
                    j += 1
                    score +=1
                    break
                else:
                    print('EEE')
                    i = i+1
            except ValueError:
                i += 1
                pass
        if i == 3:
            j += 1
            print(f'{nums[0]} + {nums[1]} = {nums[0] + nums[1] }')
    print(f'Score: {score}')


def get_level():
    while True:
        try:
            x = int(input('Level: '))
            if x>0 and x<4:
                return x
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return [x,y]






if __name__ == "__main__":
    main()