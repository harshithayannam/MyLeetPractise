import math
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        alist = []
        blist = []
        count = 0
        for i in range(1,a+1):
            if a%i == 0:
                alist.append(i)
        for i in range(1, b+1):
            if b%i == 0:
                blist.append(i)
        for i in range(len(alist)):
            if alist[i] in blist:
                count += 1
        
        return count