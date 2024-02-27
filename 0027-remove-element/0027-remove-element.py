class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next_pos = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[next_pos] = nums[i]
                next_pos += 1
        return next_pos
        