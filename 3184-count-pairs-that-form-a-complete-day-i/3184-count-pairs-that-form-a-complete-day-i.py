class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        n = len(hours)
        count=0
        for i in range(n):
            for j in range(1,n):
                if ((hours[i] + hours[j]) % 24 == 0) and i!=j and i<j:
                    count = count + 1
        return count