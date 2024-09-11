from datetime import date
import inflect
import sys

def main():

    sample= "2001-02-13"
    input_date = input("Date of Birth: ")

    print(calc_minutes(input_date))


def calc_minutes(input_date):
    try:
        born_date = date.fromisoformat(input_date)
    except:
        sys.exit("Invalid date")

   #print(born_date)
    current_date= date.today()
    time_passed = ((current_date - born_date).days)*24*60

    p = inflect.engine()
    minutes_in_words = p.number_to_words(time_passed, andword="").capitalize()

    return f"{minutes_in_words} minutes"

if __name__ == "__main__":
    main()
