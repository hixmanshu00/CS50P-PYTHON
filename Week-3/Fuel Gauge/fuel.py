def main():
    while True:
        exp = input('Fraction: ')
        if valid(exp) == True:
            break
    e = exp.split('/')
    percent = round(int(e[0])/int(e[1]) * 100)
    if(percent<=1):
        print('E')
    elif(percent>=99):
        print('F')
    else:
        print(f'{percent}%')


def valid(exp):
    e = exp.split('/')
    if len(e)!=2 or e[1] == '0'  :
        return False
    if e[0].isnumeric() and e[1].isnumeric() and int(e[0]) <= int(e[1]):
        return True

main()