class Solution:
    def minBitFlips(self, start: int, goal: int) :
        ans=start^goal
        c=0
        while (ans!=0):
            rem=ans%2
            if rem==1:
                c+=1
            ans=ans//2
        return (c)
     
       
       
        
       