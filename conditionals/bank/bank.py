greeting= input("please enter greeting").lower().replace(" ","")
if "hello" in greeting:
    print("$0")
elif greeting[0]=="h":
    print("$20")
else:
    print("$100")
