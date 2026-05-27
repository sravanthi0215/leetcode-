class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        c=[0]*26
        for char in s:
            c[ord(char)-ord('a')]+=1
        for char in t:
            if c[ord(char)-ord('a')]==0:
                return False
            c[ord(char)-ord('a')]-=1
        return True 