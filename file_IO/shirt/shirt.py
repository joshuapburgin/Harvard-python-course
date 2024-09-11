import sys
import os
import csv
import pandas as pd
from PIL import Image,ImageOps


def main():

    input_photo= sys.argv[1].lower()
    output_photo= sys.argv[2].lower()

    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    elif not os.path.exists(input_photo):
        sys.exit("Input does not exist")
    elif output_photo[output_photo.find("."):] not in ".jpg.jpeg.png":
        sys.exit("Invalid output")
    elif input_photo[input_photo.find("."):]!=output_photo[output_photo.find("."):]:
        sys.exit("Input and output have different extensions")
    else:
        change_photo(input_photo , output_photo)

def change_photo(input_photo , output_photo):

    initial_muppet= Image.open(input_photo)
    shirt = Image.open("shirt.png")

    fitted_muppet=ImageOps.fit(initial_muppet, shirt.size)

    fitted_muppet.paste(shirt, shirt)
    fitted_muppet.save(output_photo)



if __name__ == "__main__":
    main()
