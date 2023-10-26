inp = input("Input: ")
str = ''

for c in inp:
    if c.lower() == 'a' or c.lower() == 'e' or c.lower() == 'i' or c.lower() == 'o' or c.lower() == 'u':
        continue
    else:
        str += c

print("Output:", str)