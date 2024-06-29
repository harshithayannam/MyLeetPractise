class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1set = set()
        num2set = set()
        for i in range(1, n+1):
            if i%m != 0:
                num1set.add(i)
            else:
                num2set.add(i)
                
        num1 = sum(num1set)
        num2 = sum(num2set)
        return num1-num2