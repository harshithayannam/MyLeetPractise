class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        new_nums = list(set(nums))
        for i in range(len(new_nums)):
            val = new_nums[i]
            dup = nums.count(val)
            pairs += (dup*(dup-1))//2
        return pairs
