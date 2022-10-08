def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def locate_card(cards, query):

    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid - 1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
    
    return binary_search(0, len(cards) - 1, condition)


#see tests below

tests = []

test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
}

test2 = {
   'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
}

largeTest = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998
}


#test case 1
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

#test case 2
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

#test case 3
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

#test case 4
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

#test case 5
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

#test case 6
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

#test case 7
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

#test case 7
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

#for test in tests:
#    result = locate_card(test['input']['cards'], test['input']['query'])
#    print(result == test['output'])


# Ascending array test
ascending_array_test = {
    'input': {
        'nums': [5, 7, 7, 8, 8, 10],
        'target': 8
    },
    'output': [3, 4]
}

# Given an array of integers num sorted in ascending order, find the starting and ending position of a given number

# this differs from the problem in only two significant ways
# 1. The numbers are sorted in increasing order
# 2. We are looking for the start index and the end index

def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'

    return binary_search(0, len(nums) - 1, condition)

def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums) - 1 and nums[mid + 1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums) - 1, condition)


def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)

result = first_and_last_position(ascending_array_test['input']['nums'], ascending_array_test['input']['target'])
print("result:", result)
result2 = []
result2.append(first_position(ascending_array_test['input']['nums'], ascending_array_test['input']['target']))
result2.append(last_position(ascending_array_test['input']['nums'], ascending_array_test['input']['target']))
print('result array:', result2)
print(result2 == ascending_array_test['output'])
