import CSV

superheroes[]

with open("superheroes.csv") as file:
    reader= csv.DictReader(file)
    for row in reader:
        superheros.append({"name": row["name"], "lore": row["lore"]})


for superhero in sorted(superheroes, key=lambda  superhero: superhero["name"]):
    print(f"{superhero['name']} is in the {superhero['name']} universe")





with open("hello.csv") as file:
    reader= csv.DictRead(file)
    for superhero in reader:
        superheroes.append(superhero)


import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

