def cost():
    food_list={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    price=0.
    while True:
        try:
            food_item= input("Item: ").lower().title()
            if food_item not in food_list:
                    raise ValueError

            for i in food_list:

                if food_item== i:
                    price+= float(food_list[i])

            total=format(price,".2f")
            print(f"Total: ${total}")


        except ValueError:
            continue
        except EOFError:
             break

cost()
