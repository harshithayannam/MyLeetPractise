from collections import Counter 
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count1 = Counter(s)
        count2 = Counter(t)
        for letter in count2:
            if count2[letter] != count1.get(letter, 0):
                return letter
