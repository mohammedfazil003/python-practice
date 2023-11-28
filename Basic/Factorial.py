'''
    Write a Python program to find the factorial of a number without recrusion.
'''
def fact(n):
    if n<0:
        return "the given no is not a palindrome."
    elif n==0 or n==1:
        return 1
    else:
        fact =1
        while (n >1):
            fact *= n
            n -= 1
        return fact


result = fact(int(input("enter the number: ")))
print(result)