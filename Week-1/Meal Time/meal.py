def main():
    time = input("What time is it? ")
    num = convert(time)
    if num>=7.0 and num<=8.0:
        print("breakfast time")
    elif num>=12.0 and num<=13.0:
        print("lunch time")
    elif num>=18.0 and num<=19.0:
        print("dinner time")
    


def convert(time):
    arr = time.split(":")
    x = float(arr[0])
    y = float(arr[1])/60
    z = x+y
    return z


if __name__ == "__main__":
    main()