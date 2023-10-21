def main():
    str = input()
    final = convert(str)
    print(final)

def convert(str):
    if str.find(":)") != -1 :
        str =  str.replace(":)","🙂")
    if str.find(":(") != -1 :
        str = str.replace(":(","🙁")


    return str

main()