

'''Below is the 4nd task from the Basic'''



"use lists, dictionaries and tuples"

# list
basket_of_fruits = ['apple', 'cherry', 'banana', 'orange', 'plum', 'pear', 'strawberry']
for fruit in basket_of_fruits:
    print(fruit)


# tuple
tuple_made_of_list = tuple(basket_of_fruits)
print('the fruit under the index 3 is ' + str(tuple_made_of_list[3]))



# dict
basket_of_apples = {
    "red apple": 5,
    "green apple": 7,
    "yellow apple": 12,
    "strange apple": 4,
}

print("All the apples gathered today " + str(basket_of_apples))



"Use  get, add, remove elements for list structures"

# get
print(basket_of_apples.get("strange apple"))

# add
basket_of_fruits.append('avocado')

# remove
basket_of_fruits.remove('cherry')
print('the cherry did not survive ' + str(basket_of_fruits))