from collections import Counter
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        dif = sum2-sum1
        return dif//(len(nums1))