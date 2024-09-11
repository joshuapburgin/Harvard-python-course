
word= input("Enter string\t")
i=0
while i<len(word):
    if word[i]==word[i].upper():
        word= word[0:i]+"_"+word[i].lower()+word[i+1:]

    i+=1
print(word)


