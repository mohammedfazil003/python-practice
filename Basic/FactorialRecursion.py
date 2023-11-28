'''
    Write a Python program to find the factorial of a number using  recrusion.
'''

def fact(number):
    if number == 0 or number==1:
        return number
    else:
        return number * fact(number-1)


result = fact(int(input("enter the number: ")))
print(result)