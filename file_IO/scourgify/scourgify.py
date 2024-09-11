import sys
import os
import csv
import pandas as pd


def main():


    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    elif not os.path.exists(sys.argv[1]):
        sys.exit("Could not read invalid_file.csv")
    elif sys.argv[1][-4:]!=".csv":
        sys.exit("Not a CSV file")
    else:
        data_formatted=format_data(sys.argv[1])
        create_new_file(data_formatted, sys.argv[2])

def format_data(original_csv):
    # Read the original CSV
    data_original = pd.read_csv(original_csv)

    # Split the 'name' column into 'last_name' and 'first_name'
    name_split = data_original['name'].str.split(',', expand=True)
    data_original['last'] = name_split[0].str.strip()
    data_original['first'] = name_split[1].str.strip()

    # Select and rename the columns as required
    data_formatted = data_original[['first', 'last', 'house']]

    return data_formatted

def create_new_file(data_formatted, csv_formatted_name):
    # Open or create the new CSV file for writing
    data_formatted.to_csv(csv_formatted_name, index=False)

if __name__ == "__main__":
    main()
