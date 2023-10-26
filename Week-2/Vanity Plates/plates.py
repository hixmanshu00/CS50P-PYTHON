plate = input('Plate: ')
switch =  False
invalid = False

if len(plate) > 6 or len(plate)<2 :
    print('Invalid')

elif plate[0].isnumeric() == True or plate[1].isnumeric() == True or plate[2] == '0':
    print('Invalid')

else:
    for c in plate:
        if c.isspace() == True or c == ',' or c == '.' :
            print('Invalid')
            invalid = True
            break
        if c.isnumeric() == True:
            switch = True

        elif switch == True and c.isalpha() == True:
            print('Invalid')
            invalid = True
            break
    if invalid == False:
        print('Valid')


