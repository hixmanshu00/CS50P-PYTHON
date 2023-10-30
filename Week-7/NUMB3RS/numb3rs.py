import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.strip()
    if not re.search(r'^\d+\.\d+\.\d+\.\d+$',ip):
        return False
    nums = ip.split('.')
    for i in nums:
        if int(i)<0 or int(i)>255:
            return False
    return True


if __name__ == "__main__":
    main()