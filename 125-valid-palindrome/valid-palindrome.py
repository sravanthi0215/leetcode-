class Solution:
    def isAlphanumeric(self, ch):
        if(('0'<=ch<='9') or ('a'<=ch.lower()<='z')):
            return True
        return False
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        st=0
        end=n-1
        while(st<end):
            if not self.isAlphanumeric(s[st]):
                st+=1
                continue
            if not self.isAlphanumeric(s[end]):
                end-=1
                continue
            if(s[st].lower()!=s[end].lower()):
                return False
            st+=1
            end-=1
        return True

        