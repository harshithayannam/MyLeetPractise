class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        my_dict={}
        flag=0
        if len(s) ==  len(t):
            for i in range(len(s)):
                if s[i] in my_dict:
                    if my_dict[s[i]] == t[i]:
                        continue
                    else:
                        flag=1
                        break
                elif t[i] in my_dict.values():
                    flag=1
                    break
                else:
                    my_dict[s[i]]=t[i]
                    print(my_dict.values())            
        else:
            return False
        
        print(my_dict)
        if flag==1:
            return False
        # elif len(set(s))==len(my_dict):
        #     return True
        else:
            return True
        
         