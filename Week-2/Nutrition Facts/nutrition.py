x = input('Item: ')
x = x.lower()

match x:
    case 'apple':
        print('Calories: 130')
    case 'avocado':
        print('Calories: 50')
    case 'kiwifruit':
        print('Calories: 90')
    case 'pear':
        print('Calories: 100')
    case 'cherries':
        print('Calories: 100')
    case 'sweet cherries':
        print('Calories: 100')
    case _:
        print()