from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        new_nums=[0]*n
        for i in range(n):
            new_nums[(i+k)%n]=nums[i]
        for i in range(n):
            nums[i]=new_nums[i]