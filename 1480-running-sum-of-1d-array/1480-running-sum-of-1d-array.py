class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        returnsum = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            returnsum.append(total)
        
        return returnsum