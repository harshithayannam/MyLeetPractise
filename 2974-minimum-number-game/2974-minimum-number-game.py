class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        for i in range(len(nums)//2):
            alice = nums.pop(0)
            bob = nums.pop(0)
            arr.append(bob)
            arr.append(alice)
        return arr