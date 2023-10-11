class Solution:
    def reverseBits(self, n: int) -> int:
        n=bin(n)[2:].zfill(32)
        
        temp=''
        if len(n)==32:
            for i in range(len(n)-1,-1,-1):
                temp+=n[i]
        
        return(int(temp,2))