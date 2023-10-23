x = input("Greeting: ")
x = x.lower()
x = x.strip()
if x[0] == 'h' and x.find('hello') ==-1:
    x=0

elif x.find('hello') != -1:
    x = "hello"

match x:
    case "hello":
        print("$0")
    case 0:
        print("$20")
    case _:
        print("$100")