class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m*k>n:
            return -1
        minDay,maxDay=min(bloomDay),max(bloomDay)
        ans=-1
        while(minDay<=maxDay):
            days=minDay+(maxDay-minDay)//2
            if self.canMake(bloomDay,days,m,k):
                ans=days
                maxDay=days-1
            else:
                minDay=days+1
        return ans
    def canMake(self,bloomDay,days,m,k):
        count,b=0,0
        for i in bloomDay:
            if days>=i:
                count+=1
                if(count==k):
                    b+=1
                    count=0
            else:
                count=0          
        return b>=m
            

