class Solution:
    def isHappy(self, n: int) -> bool:
        val = set()
        while n != 1 and n not in val:
            val.add(n)
            print(val)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1