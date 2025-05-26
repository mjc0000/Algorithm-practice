
from typing import List



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]

        nums.sort()

        for i in range(len(nums)-2):
            if i>0 and nums[i]<nums[i-1]:
                continue

            left = i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total<0:
                    left+=1
                elif total>0:
                    right-=1
                else:
                    result.append([[nums[i],nums[left]],nums[right]])

            while left<right and nums[left]==nums ==nums[left+1]:
                left+=1
            while left<right and nums[right] ==nums[right-1]:
                right-=1

            left=+1
            right-=1

        return result




nums1 = [-1,0,1,2,-1,-4]
solution=Solution()
print(solution.threeSum(nums1))