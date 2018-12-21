def checkPossibility(nums):

    if len(nums) < 3 or is_non_decreasing(nums):
        return True

    decreasing_count = 0
    for i in range(0, len(nums) - 1):
        print('comparing ' + str(nums[i]) + ' and ' + str(nums[i + 1]))
        if nums[i] > nums[i + 1]:
            decreasing_count = decreasing_count + 1
            if decreasing_count > 1:
                return False
            if is_non_decreasing(nums[:i] + nums[i + 1:]):
                return True
            if len(nums) >= (i + 2) and is_non_decreasing(nums[:i + 1] + nums[i + 2:]):
                return True
    return False


def is_non_decreasing(nums):
    print('checking if ' + str(nums) + ' is non decreasing')
    for i in range(0, len(nums) - 1):
        print('looking at ' + str(nums[i]) + ' and ' + str(nums[i + 1]))
        if nums[i] > nums[i + 1]:
            print('it is decreasing')
            return False
    return True

# only increasing or staying the same

# print(isNonDecreasing([1, 2, 3]))
# print(checkPossibility([3, 4, 2, 3]))  # should be false
# print(checkPossibility([4, 2, 1]))  # should be false
# print(checkPossibility([1, 2, 3]))  # should be True
# print(checkPossibility([2, 3, 3, 2, 4]))  # should be True
print(checkPossibility([1, 2, 4, 5, 3]))  # should be True