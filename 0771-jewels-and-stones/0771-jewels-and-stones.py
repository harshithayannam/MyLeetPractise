from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = Counter(stones)
        types = 0
        for ch in jewels:
            types = types + count[ch]
        
        return types