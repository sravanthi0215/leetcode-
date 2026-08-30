class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        minDay=min(bloomDay)
        maxDay=max(bloomDay)
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
        count=0
        b=0
        for i in bloomDay:
            if days>=i:
                count+=1
                if(count==k):
                    b+=1
                    count=0
            else:
                count=0
            
        if(b>=m):
            return True

