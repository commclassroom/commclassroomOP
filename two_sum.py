target = 6

nums = [1,2,3,4,5]
n = len(nums)
for i in range(n):
    for j in range(n):
        if nums[i]+nums[j]==target:
            print(True)
