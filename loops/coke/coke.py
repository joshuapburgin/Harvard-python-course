def change_owed():
    owed=50
    while True:
        paid= int(input("please enter amount paid\t"))
        if valid_amount(paid):

            owed-=paid

            if owed>0:
                print(f"Amount Due: {owed}")
            else:
                print(f"Change Owed: {-owed}")
                break
        else:
            print(f"Amount Due: {owed}")



def valid_amount(paid):
    valid_coin=False
    match paid:
        case 5| 10 | 25 | 50:
            valid_coin=True

    return valid_coin



change_owed()
