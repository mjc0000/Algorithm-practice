class Solution:
    def isValid(self,s: str) ->bool:
        stack =[]
        mapping = {')':'(','}':'{',']':'['}  #字典形式

        for char in s:
            if char in mapping.values():
                stack.append(char)

            elif char in mapping:

                if not stack or stack.pop() !=mapping[char]:
                    return False
        return  len(stack) ==0
