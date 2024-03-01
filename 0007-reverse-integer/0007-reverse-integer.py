class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        v = x
        if x<0:
            x = -(x)
        while x>0:
            last_dig = x % 10
            if rev> (2 **31 -1)//10:
                return 0
            rev = rev*10+last_dig
            x=x//10
        if v<0:
            return -(rev)
        else:
            if -(2 **31) <=rev <=(2**31 -1):
                return rev
            else:
                return 0