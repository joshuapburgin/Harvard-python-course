import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    portion= ip.split(".")
    if first_portion := re.search(r"[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]", portion[0]):
        if matches := re.search(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", ip):
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
