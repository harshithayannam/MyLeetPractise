class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        u=[char for char in s if char.isalpha()][::-1]
        l=[]
        index=0
        for char in s:
            if char.isalpha():
                l.append(u[index])
                index= index+1
            else:
                l.append(char)
        val = "".join(l)
        return val
        