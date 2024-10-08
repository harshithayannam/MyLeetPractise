class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzeropos = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[nonzeropos] = nums[i]
                nonzeropos += 1
        
        for i in range(nonzeropos, len(nums)):
            nums[i] =0
        
