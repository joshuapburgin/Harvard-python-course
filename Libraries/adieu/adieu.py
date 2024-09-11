


def song():
    name_input=[]
    while True:
        try:
            name_input.append(input("Name: ").strip().title())

        except EOFError:
            break
    output=""
    length=len(name_input)
    for i in range(length):
        if length==2:
            output=name_input[0]+" and "+name_input[1]
        elif length!=1:
            if i!=(length-1):
                output+=name_input[i]+", "
            else:
                output+="and "+name_input[i]
        else:
            output=name_input[0]

    print("Adieu, adieu, to "+output)

if __name__ == "__main__":
    song()
