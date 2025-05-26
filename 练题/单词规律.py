class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        long=len(pattern)
        dic_line_to_s={}
        dic_s_to_line={}
        line=s.split()
        if len(line)!=long:
            return False

        else:
            for i in range(long):
                if line[i] not in dic_line_to_s:
                    dic_line_to_s[line[i]]=pattern[i]
                elif dic_line_to_s[line[i]]!=pattern[i]:
                    return False

                if line[i] not in dic_s_to_line:
                    dic_s_to_line[pattern[i]]=line[i]
                elif dic_s_to_line[pattern[i]]!=line[i]:
                    return False
                else:
                    pass
            return True