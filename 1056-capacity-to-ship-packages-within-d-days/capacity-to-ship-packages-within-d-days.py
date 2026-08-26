class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        ans=high

        while(low<=high):
            cap=(low+high)//2
            if self.canShip(cap,weights,days):
                ans=cap
                high=cap-1
            else:
                low=cap+1
        return ans
    def canShip(self,cap,weights,days):
        curr=0
        day=1
        for i in weights:
            if curr+i>cap:
                day+=1
                curr=i
            else:
                curr+=i
        return day<=days

            
                

        