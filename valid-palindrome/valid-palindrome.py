import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ''.join(filter(str.isalnum, s))
        rev_new_s = new_s[::-1]
        return new_s == rev_new_s
        
            