class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealthmax=0
        for acc in accounts:
            wealth = sum(acc)
            if wealth > wealthmax:
                wealthmax = wealth
        return wealthmax