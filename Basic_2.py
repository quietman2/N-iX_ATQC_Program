'''Below is the 2nd task from the Basic'''

"use conditions 'if' and  'case'" \
"Create 4 boolean variables(true,true,false,false) and compare them between themselves - " \
"result print in console. · "
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

"· Create 2 different strings. Compare them with usage if trinar operator and print 'Not equal', 'Equal' and explain."

some_text = 'laptop cooling stand'
some_text2 = 'laptop cooling stand'

if some_text != some_text2:
    print('Not equal')
else:
    print('Equal')  # 'add an explanation'






"· Explain the difference between &, |, &&, || and provide an example."




'· Create 2 string variables with the same value but initialize one with literal and another with a constructor.' \
' (String a =\'lalala\'; String b = new String(\'lalala\');)' \
' Compare these values with usage of == and equal. Explain the result'

a = "lalala"
b = str(a)

print(a == b) # 'add an explanation'
