class Solution:
    def scoreOfString(self, s: str) -> int:
        asc = []
        for ch in s:
            asc.append(ord(ch))
        total_list = []
        total = 0
        for i in range(len(asc)-1):
            total_list.append(abs(asc[i] - asc[i+1]))
            total = sum(total_list)
        return total