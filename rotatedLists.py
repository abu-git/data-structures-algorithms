#   You are giving list of numbers, obtained by rotating a sorted list an unknown number of times
#   Write a function to determine the minimum number of times the original sorted list was rotated
#   to obtain given list. Your function should have the warst case complexity of O(log N) where N
#   is the length of the list. You can sssume all the numbers in the list are unique.


#   Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9]
#   3 times

#   We define 'rotating a list' as removing the last element of the list and adding it before the first
#   element. Eg rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4]

#   Sorted list refers to a list where the elements are arranged in the increasing order eg [1, 3, 5, 7]



def count_rotations(nums):
    # initial value of position
    position = 1

    while position <= len(nums) - 1:
        if nums[position] < nums[position - 1]:
            return position
        position+=1
    return 0

#   see tests below
tests = []

#   a list of size 10 rotated 3 times
tests.append({
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
})

#   a list of size 8 rotated 5 times
tests.append({
    'input': {
        'nums': [4, 5, 6, 7, 8, 1, 2, 3]
    },
    'output': 5
})

#   a list that was not rotated at all
tests.append({
    'input': {
        'nums': [2, 4, 7, 8]
    },
    'output': 0
})

#   a list that was rotated once
tests.append({
    'input': {
        'nums': [7, 3, 5]
    },
    'output': 1
})

#   a list rotated n-1 times where n is the size of the list
tests.append({
    'input': {
        'nums': [5, 6, 8, 9, 2]
    },
    'output': 4
})

#   a list that was rotated n times
tests.append({
    'input': {
        'nums': [3, 5, 7, 8, 9, 10]
    },
    'output': 0
})

#   an empty list
tests.append({
    'input': {
        'nums': []
    },
    'output': 0
})

#   a list containing one element
tests.append({
    'input': {
        'nums': [5]
    },
    'output': 0
})

for test in tests:
    result = count_rotations(test['input']['nums'])
    print(result == test['output'])