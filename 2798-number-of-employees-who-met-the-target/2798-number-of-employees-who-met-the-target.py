class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort()
        count = 0
        for i in range(len(hours)):
            if hours[i]>= target:
                count = count + 1
        return count