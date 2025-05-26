class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s_to_t={}
        dic_t_to_s={}
        if(len(s)!=len(t)):

            return False
        else:
            for i in range(len(s)):
                if s[i] not in dic_s_to_t:
                    dic_s_to_t[s[i]]=t[i]
                elif dic_s_to_t[s[i]]!=t[i]:
                    return False
                else:
                    pass

                if t[i] not in dic_t_to_s:
                    dic_t_to_s[t[i]]=s[i]
                elif dic_t_to_s[t[i]]!=s[i]:
                    return False
                else:
                    pass
            return True