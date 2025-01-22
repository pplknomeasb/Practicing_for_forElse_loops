# What I am wanting to do is put my study to practice


myList = ["Pontiac", "Cadillac", "Toyota", "Chevrolet", "Buick", "Audi", "Dodge"]

for cars in myList:
    print(cars.upper())
else:
    print("Vroom Vroom")
    print()

for index, element in enumerate(myList):
    print(index + 1, element.lower())
else:
    print("More Vroomies! The first index being the 0's place is annoying, so I changed it to one by adding 1 to each index")
    print()

myCar = "Sonata"

for letter in myCar:
    print(letter.upper())