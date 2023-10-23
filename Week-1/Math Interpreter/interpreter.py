exp = input("Expression: ")
arr = exp.split(" ")
x = float(arr[0])
y = arr[1]
z = float(arr[2])

match y:
    case '+':
        print(x+z)
    case '-':
        print(x-z)
    case '/':
        print(x/z)
    case '*':
        print(x*z)