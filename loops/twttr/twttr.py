def vowel_removal():
    word=input("enter string ").strip()
    vowels="aeoiuAEOIU"
    new_word=""
    for i in word:
        if i not in vowels:
            new_word+=i
    print(new_word)
vowel_removal()

