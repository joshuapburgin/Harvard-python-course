def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):

    length=len(plate)
    disallowed_characters= " .,?"
    number_count=0
    two_letter=plate[0:2]
    digits=""

    if two_letter.isdigit() or not 2<=length<=6:
        return False
    if plate.isdigit() and plate[-1].isalpha():
        return False
    elif plate.isalpha() and plate[-1].isalpha():
        return True

    for char in plate:
        if char in disallowed_characters:
            return False
        if char.isdigit():
            digits+=char

    for i in range(length):
        if plate[i-1].isdigit() and plate[i].isalpha()and plate[i+1].isdigit():
            return False

    if digits[0]=="0":
        return False


    return True

if __name__ == "__main__":
    main()
