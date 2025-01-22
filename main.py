from functools import reduce

vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]

##Basic loop
for each_vendor in vendors:
    print(each_vendor)
else:
    print("The end of the basic for loop has been reached")

##This len function results 5, integer
len(vendors)

##The list always beings in the 0's place
list(range(5))

##Now are going to create a list after printing the elements
print()
for element_index in range(len(vendors)):
    print(vendors[element_index])
else:
    print("The end of the list building for loop has been reached")
print()

##We're going to print the elements in the list with the index included
##The enumerate function allows index to hold the place value
##The enumerate function allows element to hold the contents of that place value
for index, element in enumerate(vendors):
    print(index, element)
else:
    print("The end of the list practicing using the enumerate function has been reached.")
print()

mystring = "Cisco"

for letter in mystring:
    print(letter)
    print(letter*2)
    print(letter*3)
else:
    print("We've reached of the end of the for loop practicing creating a list with the string inputted.")

print()
print()

r = range(10)

for i in r:
    print(i * 2)

print("We must remember that the first place in any array begins with the 0's place")
