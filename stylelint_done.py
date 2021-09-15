# CODE SOURCE: SOFTWARE ARCHITECTURE WITH PYTHON

###################################################################################
#
# Original code to be fixed:
#
# def factorial(n):
# if n == 0:
# return 1
# else:
# return n*factorial(n-1)
####################################################################################


# It's necessary to fix identation:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Input a number to see the factorial : ")) #receive input from user
print(factorial(n)) # printing the result



