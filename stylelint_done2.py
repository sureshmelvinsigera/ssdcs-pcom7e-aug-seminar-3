####################################################################################
# Another version:factorial function is defined only for positive integers
####################################################################################
# The factorial function where input is a non-negative integer

def factorial(n):
    if n < 0 or type(n) is float:
        return("Number cannot be negative or floating point!")
    return 1 if n == 0 else n * factorial(n - 1)

n=abs(int(input("Input a number to see the factorial : ")))
print(factorial(n))
