from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i] !=val:
                nums[k]=nums[i]
                k+=1
        return k


'''
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        new_nums=[0]*n#这样定义List列表
        a=0
        for i in range(n):
            if nums[i]==val:
                continue
            else:
                new_nums[a]=nums[i]

            a+=1
        b=a

        while n-a>0:
            new_nums[a]='_'


        nums=new_nums

nums = new_nums 这行代码使得 nums
指向了新的列表 new_nums，
而不是在原列表基础上进行修改，这就违背了题目原地修改数组的要求。
并且，在调用这个函数时，外部传入的 nums 列表不会因为这个赋值操作而改变，
因为 Python 中函数参数传递是值传递（对于列表等可变对象，传递的是对象的引用，
但这里的赋值操作改变了引用指向）。

        return b
'''



