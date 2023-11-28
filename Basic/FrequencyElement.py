'''
    Write a program to count the frequency of each element in a list.
'''

def frequency_count(nums):
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency


nums = [1, 2, 1, 3, 2, 1, 4, 4, 5]
frequency = frequency_count(nums)

for number, freq in frequency.items():
    print(f"the frequency of number {number} is  {freq}")