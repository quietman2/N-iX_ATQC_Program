

"Below is the 3rd task from the Basic"



"· Create for, while, do while cycles that iterate 10 times and print iteration number to console. · "

for i in range(1, 11):
    print('for loop iteration number ' + str(i))

v = 1
while v <= 10:
    print('while loop iteration number ' + str(v))
    v += 1

# 'do while' cycle is not represented in Python 3



"Create recursion with exit condition. "

def recursive(num):
    if num >= 10:
        return num
    return recursive(num + 1)
x = recursive(3)
print(x)



"· Create an infinite loop."

"""
while 1 > 0:
    print('loping...')

"""



"· Create recursion without exit condition."

def recursive_fibonacci(n):
   if n <= 1:
       return n
   else:
       x = recursive_fibonacci(n-1)
       y = recursive_fibonacci(n-2)
       return x + y

print(recursive_fibonacci(10))