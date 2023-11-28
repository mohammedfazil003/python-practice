'''
Write a program to check if a number is prime.
'''
def isPrime(number):
    if (number < 2):
        return False
    else:
        for i in range(2, int(number/2)+1):
            if number %i == 0:
                return False
        return True


number = isPrime(int(input("enter a number: ")))
print(number)