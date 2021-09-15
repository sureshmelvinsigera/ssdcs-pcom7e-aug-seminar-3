####################################################################################
# Three ways to calculate factorial:
# a) Using a function from the math module;
# b) Using for loop;
# c) Using recursion.
####################################################################################


# a) Using a function from the math module:

from math import factorial

fac = factorial(n)
print(fac)


# b) Using for loop:

def iter_factorial(n):
    factorial = 1
    n = input("Enter a number: ")  # c) Using recursion:
    factorial = 1
    if int(n) >= 1:
        for i in range(1, int(n) + 1):
            factorial = factorial * i
        return factorial


num = int(input("Enter the number: "))

print("factorial of ", num, " (iterative): ", end="")
