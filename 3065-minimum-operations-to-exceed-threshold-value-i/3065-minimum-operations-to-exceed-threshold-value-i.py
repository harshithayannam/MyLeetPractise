class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        i = 0
        while i<len(nums):
            if nums[i]<k:
                nums.pop(i)
                count = count + 1
            else:
                break
        return count
                
            