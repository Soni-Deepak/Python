'''

Factorial(0) = 1
Factorial(1) = 1
Factorial(5) = 5 X 4 X 3 X 2 X 1
Factorial(n) = n X (n-1) X ......  X 4 X 3 X 2 X 1


Factorial(n) = n X Factorial(n-1)

'''

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n-1)


n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")