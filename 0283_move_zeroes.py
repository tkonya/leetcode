def moveZXeroes(nums):

    if len(nums) < 2:
        return nums

    keep_going = True
    while keep_going:
        keep_going = False
        for i in range(1, len(nums)):
            if nums[i - 1] == 0 and nums[i] != 0:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                keep_going = True

    return nums

print(moveZXeroes([0, 1, 0, 3, 12]))


