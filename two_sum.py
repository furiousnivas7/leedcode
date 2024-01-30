l1=input()
nums=[int(n) for n in l1.split(",")]
target = int(input())
for i in nums:
    for j in range(1,len(nums)):
        if((i+nums[j])==target):
            a = nums.index(i)
            b = j
l2=[]
l2.append(a)
l2.append(b)
print(l2)

num_str= input()
target = int(input())


nums = [int(n) for n in num_str.split()]

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i] == target-nums[j]:
                    return [i, j]
solution = Solution()
print(solution.twoSum(nums, target))
