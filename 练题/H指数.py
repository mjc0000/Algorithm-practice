from tkinter import Listbox
from typing import List

#class Solution:

def hIndex(self, citations: List[int]) -> int:
    may_h_max = len(citations)
    for i in range(may_h_max + 1):
        may_h = may_h_max - i
        count = 0
        for i in citations:
            if i >= may_h:
                count += 1

        if count >= may_h:
            return may_h

citation  = [1,3,1]
print(hIndex( citation,citation )  )
