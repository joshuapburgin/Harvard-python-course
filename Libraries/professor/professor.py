import random


def main():

    level= get_level()

    points=0

    for j in range(10):
        number_x,number_y = generate_integer(level)
        calculation= number_x + number_y

        i=0
        while i!=3:
            attempt=int(input(f"{number_x} + {number_y} = "))
            i+=1
            if attempt==calculation:
                points+=1
                break
            else:
                print("EEE")
        if attempt!=calculation:
            print(f"{number_x} + {number_y} = {calculation}")

    print(points)

def get_level():
    while True:
        try:
            number_input= int(input("Level "))
            if number_input in [1,2,3]:
                return number_input
            else:
                raise ValueError
        except ValueError:
            continue



def generate_integer(level):


    if level==1:
        min=0
        max=9
    elif level==2:
        min=10
        max=99
    else:
        min=100
        max=999

    number_x= random.randint(min, max)
    number_y= random.randint(min, max)

    return number_x,number_y


if __name__ == "__main__":
    main()
