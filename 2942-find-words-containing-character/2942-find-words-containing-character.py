class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)):
            for char in words[i]:
                if x == char:
                    ans.append(i)
        
        return list(set(ans))