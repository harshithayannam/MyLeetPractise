import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower().translate(str.maketrans('','',string.punctuation))
        l=s.split(" ")
        s=''
        for i in range(len(l)):
            s+=l[i]
        return s==s[::-1]
            