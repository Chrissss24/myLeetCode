nums = [-1,2,1,-4,5,2,-4]
target = -8

nums.sort()
# j = len(nums) - 1
ori_sum = nums[0] + nums[1] + nums[len(nums) - 1]
# data = abs(mysum - target)
# temp = 0
result = ori_sum

for i in range(len(nums)):
    l = i + 1
    r = len(nums) - 1

    while l < r:
        mysum = nums[i] + nums[l] + nums[r]
        if abs(mysum - target) < abs(result - target):
            result = mysum
        if abs(mysum - target) == 0:
            print(mysum)
        if mysum < target:
            l += 1
        else:
            r -= 1
print("result: " + str(result))