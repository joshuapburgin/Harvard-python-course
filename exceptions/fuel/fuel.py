

def get_int():
    while True:

        try:
            prompt="enter a fraction "
            guage_string=input(prompt)
            guage_x= int(guage_string[0:guage_string.find("/")])
            guage_y= int(guage_string[guage_string.find("/")+1:])

            if guage_x>guage_y:
                raise ValueError

            guage_number=int(round(guage_x/guage_y*100,0))
            if guage_number<=1:
                print("E")
                break
            elif guage_number>=99:
                print("F")
                break
            else:
                print(f"{guage_number}%")
                break



        except ValueError:
            continue
        except ZeroDivisionError:
            continue




get_int()

