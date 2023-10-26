month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    x = input('Date: ')
    x = x.capitalize()
    x = x.strip()
    if x.find('/') == -1 and x.find(',') == -1:
     continue
    elif x.find('/') != -1:
        d = x.split('/')
        if(d[0].isnumeric()==True):
            if int(d[0]) <= 12 and int(d[1]) <=31:
                print(f'{d[2].strip()}-{int(d[0]):02}-{int(d[1]):02}',end="")
                break
    elif x.index(',') != -1:
        date = x.split(',')
        md = date[0].split(' ')
        y = date[1]
        try:
            m = month.index(md[0]) + 1
        except ValueError:
            pass
        else:
            d = md[1]
            if int(d) <= 31:
                print(f'{y.strip()}-{int(m):02}-{int(d):02}',end="")
                break




