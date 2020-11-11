

"Below is the 4th and 5th tasks from the Basic"



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
"list"
basket_of_fruits[3]
"dict"
basket_of_apples.get("strange apple")
basket_of_apples["yellow apple"]

# add
"list"
basket_of_fruits.append('avocado')
basket_of_fruits.extend('more avocados')
basket_of_fruits.insert(7, 'pineapple')
basket_of_fruits[2] = 'better banana'
"dict"
basket_of_apples["brown apple"] = 6   # add
basket_of_apples["brown apple"] = 8   # change

# remove
"list"
basket_of_fruits.remove('cherry')
basket_of_fruits.clear()

"dict"
del basket_of_apples["strange apple"]