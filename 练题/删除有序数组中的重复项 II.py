from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        a=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[a-2]:
                nums[a]=nums[i]
                a+=1
        return a





'''
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=2
        for i in range(2,len(nums)):
            if nums[i-2]==nums[i-1]:
                if nums[i]==nums[i-1]:
                    n=1
                    while nums[i]==nums[i+n]:
                        n+=1
                    nums[i] = nums[i + n]

            a+=1

        return a

#删除有序数组中的重复项 的变体
'''