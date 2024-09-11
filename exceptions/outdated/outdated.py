def format_date():
    while True:
        try:
            date_input=input("Date: ")
            bad_date= date_input.title().strip().replace(" ","/").replace(",","")

            date_portion=bad_date.split("/")
            month_portion= date_portion[0]
            day_portion= int(date_portion[1])
            year_portion= date_portion[2]

            number_month= get_month_number(month_portion)

            if int(number_month)>12 or day_portion>31 or int(year_portion)>9999 or len(date_portion)!=3:
                raise ValueError
            if not any(char in date_input for char in [",","/"]):
                raise ValueError

            contains_letters = any(char.isalpha() for char in date_input)

            # Check if there are any numbers
            contains_numbers = any(char.isdigit() for char in date_input)

            # Check if there is a slash
            contains_slash = "/" in date_input

            if contains_letters and contains_numbers and contains_slash:
                raise ValueError


        except ValueError:
            continue
        else:
            formatted_month= f"{number_month:02}"
            formatted_day= f"{day_portion:02}"
            print(f"{year_portion}-{formatted_month}-{formatted_day}")
            break


def change_monthlist():
    month_list=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    month_list= [ (i,month) for i, month in enumerate(month_list, start=1)]
    return month_list

def get_month_number(month_in_words):
    month_list= change_monthlist()
    for num_month, month in month_list:
        if(month_in_words==month):
            return num_month
    return int(month_in_words)

format_date()
