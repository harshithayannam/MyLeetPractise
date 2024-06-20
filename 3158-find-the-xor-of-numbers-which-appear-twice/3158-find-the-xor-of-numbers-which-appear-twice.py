from collections import Counter
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        val = []
        count = Counter(nums)
        for num in count:
            if count[num]>1:
                val.append(num)
        if len(val) == 0:
            return 0
        xor = val[0]
        if len(val) == 1:
            return xor
        for i in range(1, len(val)):
            xor = xor ^ val[i]
        return xor            