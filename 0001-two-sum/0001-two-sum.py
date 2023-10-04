class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lis={}
        for i in range(len(nums)):
            if (target - nums[i]) in lis:
                return [lis[target-nums[i]], i]
            lis[nums[i]]= i

