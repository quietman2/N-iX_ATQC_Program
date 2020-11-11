
"Below is the 2nd task from the Basic"

"use conditions 'if' and  'case'" # the 'case' condition is not represented in Python 3

"Create 4 boolean variables(true,true,false,false) and compare them between themselves - " \
"result print in console."
boolN1 = True
boolN2 = True
boolN3 = False
boolN4 = False

boolNresult = boolN1 == boolN2 == boolN3 == boolN4
print("Result of comparing boolean variables is " + str(boolNresult))


" · Create 4 different numeric variables and compare them with the usage of <, <=, !=, ==, ===, >=, >. " \
"Explain the result. "
numeric_var1 = 53
numeric_var2 = 553
numeric_var3 = 255
numeric_var4 = 100500


'Comparison operators are used to compare two values'
print(numeric_var1 < numeric_var2)  # returns True because 53 is less than 553
print(numeric_var1 > numeric_var2)  # returns False because 53 is not greater than 553
print(numeric_var2 <= numeric_var1)  # returns False because 553 is neither less than or equal to 53
print(numeric_var2 >= numeric_var3)  # returns True because 553 is greater, or equal, to 255
print(numeric_var3 == numeric_var4)  # returns False because 255 is not equal to 100500
print(numeric_var3 != numeric_var4)  # returns True because 255 is not equal to 100500



"· Create 2 different strings. Compare them with usage if ternary operator and print 'Not equal', 'Equal' and explain."
some_text = 'laptop'
some_text2 = 'leptop'

some_text_result = 'Equal' if some_text == some_text2 else 'Not equal'
print(some_text_result)
# ternary operator evaluates something based on a condition being true or not



"· Explain the difference between &, |, &&, || and provide an example." # the '&&' and '||' operators are not represented in Python 3

# '&', '|' are bitwise operators 'and', 'or' correspondingly

#------- Binary AND -------
a = 50     # 110010
b = 55     # 110111
c = a & b  # 110010 - the result is calculated accordingly to the 'AND' principle
print("the result of binary 'AND' operation is " + str(c))

#------- Binary OR -------
a = 50     # 110010
b = 55     # 110111
c = a | b  # 110111 - the result is calculated accordingly to the 'OR' principle
print("the result of binary 'OR' operation is " + str(c))



'· Create 2 string variables with the same value but initialize one with literal and another with a constructor.' \
' (String a =\'lalala\'; String b = new String(\'lalala\');)' \
' Compare these values with usage of == and equal. Explain the result'

a = 'lalala'
b = str('lalala') # The str() function converts the specified value into a string

print(a == b) # Returns True because 'a' and 'b' include the same string literals
