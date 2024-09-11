def shopping_list():
    groceries=[]
    while True:

        try:
            grocery= input("").strip().upper()
            groceries.append(grocery)

        except EOFError:
            break

    grocery_count={}
    for item in groceries:
        if item in grocery_count:
            grocery_count[item]+=1
        else:
            grocery_count[item]=1

    for item, count in sorted(grocery_count.items()):
        print(f"{count} {item}")


shopping_list()
