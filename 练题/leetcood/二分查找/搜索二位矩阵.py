'''class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        return False
'''
from unittest.mock import right


#二分做法：
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=m*n-1

        while left<=right:
            mid=(left+right)//2
            row=mid//n
            col=mid%n
            mid_value=matrix[row][col]

            if mid_value==target:
                return True
            elif mid_value<target:
                left=mid+1
            else:
                right=mid-1

        return False