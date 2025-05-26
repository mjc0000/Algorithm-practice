'''
为了实现找出每天之后下一个更高温度出现的天数，最快的算法可以使用单调栈。
单调栈是一种特殊的栈结构，它能保证栈内元素是单调递增或单调递减的。
在这个问题中，我们使用单调递减栈，从左到右遍历温度数组，
对于每个温度，将其索引压入栈中，如果当前温度比栈顶索引对应的温度高，
就意味着找到了栈顶索引对应的下一个更高温度，
计算天数并更新结果数组，然后弹出栈顶元素，继续比较，
直到栈为空或者当前温度小于等于栈顶索引对应的温度，
再将当前温度的索引压入栈中。
'''

from typing import List
class Solution:
    def dailyTemperatures(self,temperatures: List[int])->List[int]:
        n=len(temperatures)
        answer=[0]*n
        stack=[]
        for i in range(n):
            while stack and temperatures[i] >temperatures[stack[-1]]:
                prev_index=stack.pop()
                answer[prev_index]=i-prev_index
            stack.append(i)
        return answer


            #截止日期：2025年4月7日22:19:31  明天继续