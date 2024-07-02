class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        output = ""
        if ch not in word:
            return word
        
        for i in range(len(word)):
            if word[i] == ch:
                n =i
                break
        for i in range(n, -1, -1):
            output = output + word[i]
            
        for i in range(n+1, len(word)):
            output = output + word[i]
            
        return (output)
            
                