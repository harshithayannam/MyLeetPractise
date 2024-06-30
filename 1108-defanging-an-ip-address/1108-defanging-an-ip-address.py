class Solution:
    def defangIPaddr(self, address: str) -> str:
        ad = ''
        for ch in address:
            if ch == ".":
                ad+= f"[{ch}]"
            else:
                ad+= ch
        
        return ad