due = 50

while due > 0:
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))

    if coin == 5 :
        due -= 5
    elif coin == 10:
        due -= 10
    elif coin == 25:
        due -= 25
    if due == 0:
        print("Change Owed: 0")
    if due<0 :
        print("Change Owed:", abs(due))

