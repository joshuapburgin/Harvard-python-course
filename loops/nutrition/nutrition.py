input_fruit= input("enter fruit ").lower().strip()

input_fruit=input_fruit[0].upper()+input_fruit[1:]

if " " in input_fruit:
    input_fruit= input_fruit[0: input_fruit.find(" ")+1]+ input_fruit[input_fruit.find(" ")+1].upper()+input_fruit[input_fruit.find(" ")+2:]



fruits=[
{"name": "Apple", "calorie":"130"},
{"name": "Avocado", "calorie":"50"},
{"name": "Sweet Cherries", "calorie":"100"},
{"name": "Kiwifruit", "calorie":"90"},
{"name": "Pear", "calorie":"100"},
{"name": "Tomato", "calorie":""}
]

for fruit in fruits:
    if input_fruit==fruit["name"]:
        print(fruit["calorie"])
