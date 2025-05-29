from turtledemo.penrose import start
from typing import List

from 练题.币值转换 import result


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result=[]
        i=0
        while i<len(nums):
            start=nums[i]
            j=i
            while j+1<len(nums) and nums[j+1]==nums[j]+1:
                j+=1
            if start!=nums[j]:
                result.append(str(start) +"->"+str(nums[j]))
            else:
                result.append(str(start))

            i=j+1
        return result








'''from typing import List

废弃版本


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n=len(nums)
        result=[]
        start = nums[0]
        for i in range(n-1):
            IsFirst=True
            end=start
            if IsFirst:
                IsFirst=False
                if nums[i+1]==start+1:
                    if nums[i + 1] == start + 1:
                        pass
                    else:
                        end = nums[i]
                        part = ""
                        part += str(start)
                        part +="->"
                        part += str(end)
                        result.append(part)
                        start=nums[i+1]

            else:
                result.append(str(nums[i]))
                start=nums[i+1]
        return result



'''