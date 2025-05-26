
from typing import List




class Solution:
    def longestcommonprefix(self,strs:List[str]) ->str:
        if not strs:
            return ""
        if str == "":
           return ""


        prefix = min(len(s) for s in strs)

        for i in range(len(strs)):

            char=strs[0][i]

            for j in range(i,len(strs)):
                if strs[j][i] != char:
                    return strs[0][:i]
        return strs[0][:prefix]

strs1=["dog","racecar","car"]
solution=Solution()
fuck=solution.longestcommonprefix(strs1)

print(fuck)




