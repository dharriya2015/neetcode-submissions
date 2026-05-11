class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        if set(list(s))!=set(list(t)):
            return False
        seen={}
        for i,v in enumerate(list(s)):
            if v in seen:
                seen[v]+=1
            else:
                seen[v]=1
        
        for i,v in enumerate(list(t)):
            if v in seen:
                seen[v]-=1
                if seen[v] < 0:
                    return False
            else:
                return False
        
        return True



        # if len(s)!= len(t):
        #     return False
        # count={}
        # for char in s:
        #     count[char]= count.get(char,0) + 1
        # for char in t:
        #     if char not in count:
        #         return False
        #     count[char] -=1
        #     if count[char]<0:
        #         return False
        # return True

# from collections import Counter
# return Counter(s)==Counter(t)
