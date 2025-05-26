class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=1,2
        if n==1:
            return a
        if n==2:
            return b
        for _ in range(3,n+1):
            c=a+b
            a=b
            b=c
        return b
