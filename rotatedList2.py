#   You are given a list of numbers, obtained by rotating a sorted list an unknown number of times.
#   You are also given a target number. Write a function to find the position of the target number 
#   within the rotated list. You can assume all the numbers in the list are unique.

#   Example: In the rotated sorted list [5, 6, 9, 0, 2, 3, 4], the target number 2 occurs at position 4.


def find_target_rotated_sorted_list(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid

        #check left portion of array
        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        #check right portion of array
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
    return -1

test = {
    'input': {
        'nums': [5, 6, 9, 0, 2, 3, 4],
        'target': 2
    },
    'output': 4
}

result = find_target_rotated_sorted_list(test['input']['nums'], test['input']['target'])
print(result == test['output'])
