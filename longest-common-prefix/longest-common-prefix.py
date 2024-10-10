class Solution:
    def longestCommonPrefix(self, my_str: List[str]) -> str:
        if my_str == []:
            return ''
        if len(my_str) == 1:
            return my_str[0]
        my_str.sort()
        shortest = my_str[0]
        prefix = ''
        for i in range(len(shortest)):
            if my_str[len(my_str) - 1][i] == shortest[i]:
                prefix += my_str[len(my_str) - 1][i]
            else:
                break
        return prefix
        