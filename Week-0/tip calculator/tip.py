def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    str = d.removeprefix("$")
    return float(str)


def percent_to_float(p):
    str = p.removesuffix("%")
    return float(str)/100


main()