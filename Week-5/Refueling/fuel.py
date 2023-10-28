def main():
    print(convert('3/5'))
    print(gauge(34))


def convert(fraction):
    e = fraction.split('/')
    if int(e[0]) > int(e[1]):
        raise ValueError('X should be smaller')
    try:
        percent = round(int(e[0])/int(e[1]) * 100)
    except ZeroDivisionError:
        pass
    return percent


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()