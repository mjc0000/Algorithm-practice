from typing import List

from 练题.朋友圈 import count


#摩尔投票法
#摩尔投票法的正确性基于以下核心事实：
#多数元素的出现次数超过其他元素的总和，因此在 “抵消” 过程中必然成为最终的候选元素。

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=None
        count=0
        for num in nums:
            if count==0:
                candidate=num
                count+=1
            elif num==candidate:
                count+=1
            else:
                count-=1
        return candidate




'''
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        k=1.0*n/2
        max_number=max(nums)
        numbers=[0]*max_number
        for i in range(n):
            numbers[nums[i]]+=1

        for j in range(max_number):
            if numbers[j]>k:
                return j

'''