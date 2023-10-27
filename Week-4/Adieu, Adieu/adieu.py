import inflect
p = inflect.engine()

base = 'Adieu, adieu, to'
arr = []

while True:
    try:
        name = input('Name: ')
        arr.append(name)

    except EOFError:
        break


x = p.join(arr)
print(base,x)