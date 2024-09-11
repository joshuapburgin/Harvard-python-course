import sys
from tabulate import tabulate
import os
import csv


def main():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif not os.path.exists(sys.argv[1]):
        sys.exit("File does not exist")
    elif sys.argv[1][-4:]!=".csv":
        sys.exit("Not a CSV file")
    else:
        print(create_table(sys.argv[1]))

def create_table(csv_input):
    pizza_list=[]
    column=[]
    with open(csv_input) as file:
        reader=csv.DictReader(file)

        for row in reader:
            pizza_list.append(row)


    return tabulate(pizza_list, headers="keys" , tablefmt="grid")



if __name__ == "__main__":
    main()
