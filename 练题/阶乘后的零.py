class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factotrial(x):
            result=1
            for i in range(1,x+1):
                result*=i
            return result

        the_number=str(factotrial(n))
        the_list_number=[]
        for i in the_number:
            the_list_number.append(i)
        flag=True
        k=0
        while flag:
            if the_list_number[-k-1]=='0':
                k+=1
            else:
                flag=False

        return k


#时间复杂度为O（LogN）

'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n:
            n //= 5
            count += n
        return count
        
'''

# 0 false /// 1 true