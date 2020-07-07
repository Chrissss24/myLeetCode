nums = [2, 3, 4, 777, 888, -112, -33, -456,-2, -3, 0]
nums.sort()
# l = 0
# r = len(nums) - 1
result = []

for i in range(len(nums)):
    if nums[i] > 0 :
        break
    elif i >= 1 and nums[i] == nums[i - 1]:
        continue
    else:
        l = i + 1
        r = len(nums) - 1
        while l < r:
            mysum = nums[i] + nums[l] + nums[r]
            if mysum == 0:
                temp = [nums[i], nums[l], nums[r]]
                temp.sort()
                if temp not in result:
                    result.append(temp)
                l += 1
            if mysum > 0:
                r -= 1
            elif mysum < 0:
                l += 1
print(result)







