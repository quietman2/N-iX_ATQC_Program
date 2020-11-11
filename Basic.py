
try:

    ''' Basic variable types. Casting
    Create 5 variables with type int, long, float, double, String;
    · Assing different values to these variables and compare them. '''
    int_variable = 53
    float_variable = 5.3
    string_variable = "I'am string"
    print(int_variable == float_variable, int_variable == string_variable, float_variable == string_variable)
    # the 'long' and 'double' variables are not represented in Python 3


    " · Don't assign any values and compare variables."
    int_variable2 = None
    float_variable2 = None
    string_variable2 = None
    print(int_variable2 == float_variable2, int_variable2 == string_variable2, float_variable2 == string_variable2)


    '· Assign the same values and compare variables.'
    int_variable3 = 53
    float_variable3 = 5.3
    string_variable3 = "I'am string"
    print(int_variable == int_variable3, float_variable == float_variable3, string_variable == string_variable3)


    '· //Assign in same order [0.5,0.7,1.0,0.1] values to float and double variables and compare them.'
    float_variable4 = 0.5, 0.7, 1.0, 0.1
    float_variable5 = 0.5, 0.7, 1.0, 0.1
    print(float_variable4 == float_variable5)
    # instead of variable with double used variable with float



except:

    '· Divide numeric values by zero.'
    float_variable6 = [0.5, 0.7, 1.0, 0.1]
    result6 = None

    for i in float_variable6:
        if float_variable6:
            result6 = i / 0
    "It is not possible to divide by zero. " \
    "If we try to do this, a ZeroDivisionError is raised and the script is interrupted." \
    "The 'try', 'except', 'finally' blocks are used here to handle the error"


finally:

    '· Divide values by 3 and assign result to a variable.'
    float_variable7 = [10, 3, 53, 15]
    result7 = None

    for i in float_variable7:
        if float_variable7:
            result7 = i / 3
            print(result7)
    "Values are divided by 3 and the result is assigned to a variable" \
    "The result of a division in Python will always be a 'float number' even if an 'int number' is divided"



    '· Divide values by 3.0 and assign result and make a round operation.'
    float_variable8 = [13, 40, 33, 15]
    result8 = None

    for i in float_variable8:
        if float_variable8:
            result8 = i / 3.0
            print(round(result8))
    "function 'round()' which rounds off to the given number of digits and returns the floating point number, " \
    "if no number of digits is provided for round off , it rounds off the number to the nearest integer." \
    "result also can be rounded down by using the floor division operator: '//' "