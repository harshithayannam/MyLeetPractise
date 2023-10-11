class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        new=[]
        dup=[]
        for i in nums:
            if i not in new:
                new.append(i)
            else:
                dup.append(i)
        for j in dup:
            new.remove(j)
        
        return new[0]
