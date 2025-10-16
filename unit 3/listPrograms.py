food = ['hamburger', 'salad', 'apple', 'fries']

print(food[0]) # first item in the list
print(food[3]) # last item in the list

# replace an item in the list with a new item at the
# previous index position

food.pop(2) # remove item at specified location
print(food)
food.insert(2, 'vegan burger')
print(food) # adds item at specified location