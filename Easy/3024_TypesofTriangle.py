def triangleType(nums):
    nums.sort()
    if nums[0] + nums[1] <= nums[2]:
        return 'none'
    if nums[0] == nums[1]:
        if nums[1] == nums[2]:
            return 'equilateral'
        else:
            return 'isosceles'
    else:
        if nums[1] == nums[2]:
            return 'isosceles'
        else:
            return 'scalene'
nums = [2,3,2]
print(triangleType(nums))