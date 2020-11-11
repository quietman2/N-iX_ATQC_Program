

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


