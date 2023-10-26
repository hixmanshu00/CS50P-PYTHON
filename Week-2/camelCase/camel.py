camel = input("camelCase: ")
str = ''
split = False
for c in camel:
    if c.isupper() == True:
        c = c.lower()
        str += '_'

    str += c


print(str)

