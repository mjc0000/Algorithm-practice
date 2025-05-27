from multiprocessing.managers import ListProxy
from typing import List

from 练题.币值转换 import result


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]*len(nums)
        
        for i in range(len(nums)):
            new_nums=nums.remove(nums[i])
            k=1
            for i in new_nums:
               k=k*i
            result.append(k)
        return result


