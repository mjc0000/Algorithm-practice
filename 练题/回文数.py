class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x==0:
            return True
        if x>0:
             x=str(x)
             return x==x[::-1]