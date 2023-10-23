x = input("File name: ")
x = x.strip()
# print(x)
arr = x.split('.')
z = len(arr) - 1
y = arr[z].lower()
match y:
    case 'gif':
        print('image/gif')
    case 'jpg':
        print('image/jpeg')
    case 'jpeg':
        print('image/jpeg')
    case 'png':
        print('image/png')
    case 'pdf':
        print('application/pdf')
    case 'txt':
        print('text/plain')
    case 'zip':
        print('application/zip')
    case _:
        print('application/octet-stream')