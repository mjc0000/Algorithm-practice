from collections import Counter

from 练题.币值转换 import result


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counts=Counter(magazine)
        for i in ransomNote:
            if magazine_counts[i]<=0:
                return False
            magazine_counts[i]-=1
        return True