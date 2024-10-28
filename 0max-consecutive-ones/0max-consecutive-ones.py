class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcon = 0
        current = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
                maxcon = max(maxcon, current)
            else:
                current = 0
        
        return maxcon