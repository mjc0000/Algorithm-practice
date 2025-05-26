from typing import List #List本质上是一种动态数组。
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=1
        for i in range(1,len(nums)-1):
            if nums[i]==nums[i-1]:
                continue
            nums[a]=nums[i]
            a+=1
        return a



