class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        dim = set()
        for lis in nums:
            start, end = lis
            for point in range(start, end + 1):
                dim.add(point)
        return len(dim)