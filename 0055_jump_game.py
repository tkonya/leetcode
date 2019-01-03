def canJump(nums):
    print(nums)
    return canJumpFrom2(nums, 0)


def canJumpFrom2(nums, current_location):
    print('at location ' + str(current_location))

    if current_location >= len(nums) - 1 or current_location + nums[current_location] >= len(nums) - 1:
        # we are at the end or can reach the end
        return True

    if nums[current_location] > 0:
        # from all the possible next moves, find the one which has the furthest reach
        max_idx = furthest_reach(nums[current_location + 1:current_location + nums[current_location] + 1])
        print('jumping to max idx ' + str(current_location + max_idx + 1))
        return canJumpFrom2(nums, current_location + max_idx + 1)

    return False


def furthest_reach(nums):
    print('looking for max idx in ' + str(nums))
    max_idx = 0
    max_reach = 0
    for i in range(0, len(nums)):
        nums[i] = nums[i] + i
        if nums[i] >= max_reach:
            max_reach = nums[i]
            max_idx = i
    return max_idx


print(canJump([2, 3, 1, 1, 4]))
print(canJump([3, 2, 1, 0, 4]))
print(canJump([2, 0]))
print(canJump([1, 2, 3]))
print(canJump([1, 1, 1, 0]))
print(canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))
