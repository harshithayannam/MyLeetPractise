class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=""
        for i in digits:
            num+=str(i)
        num=int(num)
        plus=num+1
        li=[]
        l=str(plus)
        for d in l:
            li.append(int(d))
        return(li)