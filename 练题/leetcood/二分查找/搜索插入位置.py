from operator import index
from typing import List
from unittest.mock import right

from 练题.币值转换 import result


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid]==target:
                return mid
            elif nums[mid] <= target:

                left = mid + 1
            else:
                right = mid - 1
        return left#就是等价的时候，即列表里存在该数

'''
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
'''