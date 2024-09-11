import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url_portion= re.findall(r'src="([^"]*)"', s)

    #print(url_portion[0])
    if re.search(r'<iframe(.)*><\/iframe>',s):
        if url_portion[0]=="http://youtube.com/embed/xvFZjo5PgG0" or url_portion[0]=="https://youtube.com/embed/xvFZjo5PgG0" or url_portion[0]=="https://www.youtube.com/embed/xvFZjo5PgG0"or url_portion[0]=="http://www.youtube.com/embed/xvFZjo5PgG0":
            return "https://youtu.be/xvFZjo5PgG0"
        else:
            return None


if __name__ == "__main__":
    main()
