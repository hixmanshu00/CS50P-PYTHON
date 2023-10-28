def main():
    print(is_valid('fell'))


def is_valid(s):
    plate = s
    switch =  False
    invalid = False

    if len(plate) > 6 or len(plate)<2 :
        return False

    elif plate[0].isnumeric() == True or plate[1].isnumeric() == True or plate[2] == '0':
        return False
    else:
        for c in plate:
            if c.isspace() == True or c == ',' or c == '.' :
                invalid = True
                return False

            if c.isnumeric() == True:
                switch = True

            elif switch == True and c.isalpha() == True:
                invalid = True
                return False

        if invalid == False:
            return True


if __name__ == "__main__":
    main()