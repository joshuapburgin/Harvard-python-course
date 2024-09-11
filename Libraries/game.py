import random



while True:
    try:
        level= int(input("Level: "))

        if level>0:
            break

    except :
        pass
number_random= random.randint(1, level)

while True:
    try:

        number_guess= int(input("Guess: "))
        if number_guess>0:

            if number_guess>number_random:
                print("Too large!")

            elif number_guess<number_random:
                print("Too small!")

            else:
                print("Just right!")
                break
    except :
        pass






