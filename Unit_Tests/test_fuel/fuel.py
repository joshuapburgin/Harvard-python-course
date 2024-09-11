import sys

def main():

    fraction_input=input("enter a fraction ")
    converted_fraction =convert(fraction_input)
    guage_ouput= gauge(converted_fraction)
    print(guage_ouput)

def convert(fraction):

        try:

            guage_x= int(fraction[0:fraction.find("/")])
            guage_y= int(fraction[fraction.find("/")+1:])

            if guage_y==0:
                raise ValueError("denum cannot equal 0")
            if guage_x>guage_y:
                raise ValueError("Numerator should not be greater than denominator")


            percentage=int(round((guage_x/guage_y)*100,0))
            return percentage

        except ValueError:
            raise ValueError("Invalid input")

        except ZeroDivisionError:
            raise ValueError("denum cannot equal 0")

def gauge(percentage):
    if percentage<=1:
        return "E"

    elif percentage>=99:
        return "F"

    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()


