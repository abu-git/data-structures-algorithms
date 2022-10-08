# Binary Search Algorithm

# time complexity O(log N) and space complexity O(1)

def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number", mid_number)

    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def locate_cards(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        print("lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1

    return -1 

#works except for cards array with repeating numbers
#def locate_cards(cards, query):
#    lo, hi = 0, len(cards) - 1
#
#    while lo <= hi:
#        mid = (lo + hi) // 2
#        mid_number = cards[mid]
#
#        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
#
#        if mid_number == query:
#            return mid
#        elif mid_number < query:
#            hi = mid - 1
#        elif mid_number > query:
#            lo = mid + 1
#
#    return -1

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



# large array testing to compare linear search vs binary search
result = locate_cards(largeTest['input']['cards'], largeTest['input']['query'])
print(result == largeTest['output'])


#for test in tests:
#    result = locate_cards(test['input']['cards'], test['input']['query'])
#    print(result == test['output'])