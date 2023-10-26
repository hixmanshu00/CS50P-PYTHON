d = {}
while True:
    try:
        x = input()
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1
    except EOFError:
        break
keys = list(d.keys())
keys.sort()

for key in keys:
    print(f'{d[key]} {key.upper()}')
