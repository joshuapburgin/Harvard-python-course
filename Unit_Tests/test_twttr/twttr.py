def main():
    word=input("enter string ").strip()
    print(shorten(word))

def shorten(word):

    vowels="aeoiuAEOIU"
    new_word=""
    for i in word:
        if i not in vowels:
            new_word+=i
    return new_word

if __name__ == "__main__":
    main()

