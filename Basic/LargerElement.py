'''
    Write a program to find the largest element in a list.
'''

def larger_element(numbers):
    largest_num = numbers[0]
    for num in numbers:
        if num > largest_num:
            largest_num = num     
    return largest_num


numbers = [4, 10, 50, 41, 21]
print(larger_element(numbers))
