def main():
    print(value('323'))

def value(greeting):
    x = greeting.lower().strip()

    if x[0] == 'h' and x.find('hello') ==-1:
        x=0

    elif x.find('hello') != -1:
        x = "hello"

    match x:
        case "hello":
            return(0)
        case 0:
            return(20)
        case _:
            return(100)


if __name__ == "__main__":
    main()