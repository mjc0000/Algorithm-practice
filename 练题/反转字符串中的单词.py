class Solution:
    def reverseWords(self, s: str) -> str:
        line=s.split()
        new_line=line[::-1]
        new_line_plus=""+new_line[0]
        for i in new_line[1:len(new_line)+1]:
            new_line_plus=new_line_plus+" "+i
        return new_line_plus