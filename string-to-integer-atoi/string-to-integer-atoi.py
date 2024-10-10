class Solution:
    def myAtoi(self, s: str) -> int:
        int_min = -2**31
        int_max = (2**31)-1
        
        s = s.lstrip()
        
        if not s:
            return 0
    
        sign = 1
        start_index = 0
        if s[0] == '-':
            sign = -1
            start_index = 1
        elif s[0] == '+':
            sign = 1
            start_index = 1
        
        result = 0
        for i in range(start_index, len(s)):
            if s[i].isdigit():
                result = result*10 + int(s[i])
            else:
                break
        result *= sign
        if result < -2**31:
            return -2**31
        
        if result > (2**31)-1:
            return (2**31)-1
    
        return result
        