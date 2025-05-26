from typing import List


class Solution:
    def threeSum(self,nums: List[int]) ->List[List[int]]:
        result=[]
        nums.sort()
        n=len(nums)

        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=-nums[i]
            seen={}
            j=i+1
            while j<n:
                complement=target-nums[j]
                if complement in seen:
                    result.append([nums[i],complement,nums[j]])
                    while j<n-1 and nums[j]==nums[j+1]:
                        j+=1
                seen[nums[j]]=j
                j+=1
        return result
solution=Solution()

nums1 = [-1, 0, 1, 2, -1, -4]
expected1 = [[-1, -1, 2], [-1, 0, 1]]
result1 = solution.threeSum(nums1)
print(f"输入: {nums1}, 输出: {result1}, 预期输出: {expected1}, 结果是否正确: {result1 == expected1}")

# 案例 2: 没有有效三元组
nums2 = [0, 1, 1]
expected2 = []
result2 = solution.threeSum(nums2)
print(f"输入: {nums2}, 输出: {result2}, 预期输出: {expected2}, 结果是否正确: {result2 == expected2}")

# 案例 3: 只有一个有效三元组
nums3 = [0, 0, 0]
expected3 = [[0, 0, 0]]
result3 = solution.threeSum(nums3)
print(f"输入: {nums3}, 输出: {result3}, 预期输出: {expected3}, 结果是否正确: {result3 == expected3}")
