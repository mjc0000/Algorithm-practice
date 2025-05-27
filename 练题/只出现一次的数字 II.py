from collections import Counter



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq =Counter(nums)
        result=[num for num,occ in freq.items() if occ==1][0]
        return  result