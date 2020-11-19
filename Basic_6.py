import pickle
import json

"Below is the 6th task from the Basic"
from typing import List, Any

"Use 'tr- catch'  to process the exceptions. Check Exception Hierarchy.  " \
"Create a numeric variable. Divide it by zero. " \
"Handle exception and print in console exception message; "


k = 33
def this_fails():
    k / 0
try:
    this_fails()
except ArithmeticError as error:
    print("You've made a mistake. This is your error message:", error)


"Create FIle." \
"Set text into file with digits and letters, where digits are in separate line." \
"Read digits from the file and make some math operations with them"


digits = []
with open('file.txt','r') as f:
    my_file = f.readlines()
    for line in my_file:
        if line.strip().isdigit():
            digits.append(int(line))
print(digits[0] * digits[1])
print(digits[1] // digits[3])
print(digits[2] + digits[3])
print(digits[1] / digits[2])



"Create class and serialize it; print result;" \
" deserialize it; print result; // for JS serialize to JSON"

class Trainee:
    def __init__(self, name, age, project, is_on_probation):
        self.name = name
        self.age = age
        self.project = project
        self.is_on_probation = is_on_probation

trainee_1 = Trainee('Volodymyr', 30, 'Cardo', False)

pickled_trainee = pickle.dumps(trainee_1, 3)
print(pickled_trainee)

unpickled_trainee = pickle.loads(pickled_trainee)
print(unpickled_trainee)



"Create string that contains JSON { \"name\":\"John\", \"age\":30, \"car\":null }; " \
"parse this string into JSON object and print it's name and age."

str_json = '{ "name":"John", "age":30, "car":null }'
data_json = json.loads(str_json)
print(data_json['name'], data_json['age'])



"STRINGS:"

# Create 2 different strings. Concatenate them and print result. Explain what types of concatenation exists.
a = "Python is "
b = "awesome!"
print(a + b)
print(a + "awesome!")


# · Create string "   egweerw  ererferw  kuy  yu i ". Print its length;  Trim string and print result. Print length of trimmed string.
strange_string = "   egweerw  ererferw  kuy  yu i "
print("lenght of the original string is " + str(len(strange_string)))
print("this string is trimmed: " + strange_string.strip())
print("lenght of the trimmed string is " + str(len(strange_string.strip())))


# · Create string "   egweerw  ererferw  kuy  yu i ". Split string by spaces and print each value in a separate row.
for i in strange_string.split(" "):
    print(i)


# · Create string "   egweerw  ererferw  kuy  yu i ". Split string by spaces; Clean empty spaces from result; Print each result value in a separate row.
for i in strange_string.strip().split():
    print(i)


# · Create string "   egweerw  ererferw  kuy  yu i ". Convert all characters to uppercase. Print result;
print(strange_string.upper())


# · Create string "   egweerw  ererferw  kuy  yu i ". Convert all 'w' to uppercase. Print result;
print(strange_string.replace("w", "W"))


# · Create string "   egweerw  ererferw  kuy  yu i ". Convert first 'w' to uppercase. Print result;
print(strange_string.replace("w", "W", 1))

# · Create string "this item previous price $5.99, Sale price $1.99" - parse original and sale price from string and print them.
strange_string2 = "this item previous price $5.99, Sale price $1.99"

original_price = ''
sale_price = ''
for i in strange_string2:
    if i.isdigit():
        original_price += i
        sale_price += i
print(sale_price, original_price)