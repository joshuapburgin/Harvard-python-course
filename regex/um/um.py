import re
import sys


def main():
    print(count(input("Text: ")))
    #print(count("hello"))

def count(s):
    pattern=r"\b\s*(um)\s*\b"
    matches= re.findall(pattern, s, re.IGNORECASE)
    no_matches= len(matches)

    return no_matches

if __name__ == "__main__":
    main()

