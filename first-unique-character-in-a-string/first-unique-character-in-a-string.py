class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = Counter(s)
        for key, val in dic.items():
            if val!=1:
                continue
            else:
                return s.index(key)
        return -1