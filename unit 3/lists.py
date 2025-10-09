# List = a collection system for storing and organizing multiple
# pieces of data.

# List Syntax (how it is written)
# when we want to create a list, we first create a variable, and then
# assign it to the square brackets [].

# [] = square brackets mean list

shoppingList = ['apples','oranges','water',1,2,3,True,['bread','milk']]

print(shoppingList)

# If we want to access an item from a list, we use the index system.
# we write the list variable name, and then use the brackets and pass in the
# number position.

# list are zero-based -indexed; meaning the list count always starts at zero (0)

print(shoppingList[2])

trunkParty = ['fan','mini-fridge','laptop','tv','air fryer']

def addItemForCollege(list):
    newItem = input("please add neww item to college trunk party list:")
    list.append(newItem)
    print(list)

# addItemForCollege(trunkParty)

# create a function that will remove an item from the trunk party list
# use w3schools to find a list method to help you accomplish this.

def removeItemFromTrunkParty(list):
    item = input("please type the item you want to remove: ")
    list.remove(item)
    print(list)

removeItemFromTrunkParty(trunkParty)

numbersList = [100, 23, 450, 63, 1, 6, 19, 1000]

def addAndsort(newNumber):
       numbersList.append(newNumber) # new number has been added.
       numbersList.sort() # just add sort, and we are done.
       print(numbersList) # just telling the computer to print

addAndsort(60)















