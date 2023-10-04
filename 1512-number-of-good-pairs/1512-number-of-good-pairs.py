class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        result = 0
        for count in counts.values():
            result += count * (count - 1) // 2
        
        return result
        