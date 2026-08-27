class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        low=1
        high=10**7
        ans=-1
        while(low<=high):
            speed=low+(high-low)//2
            if self.canReach(dist,speed,hour):
                ans=speed
                high=speed-1
            else:
                low=speed+1
        return ans

    def canReach(self,dist,speed,hour):
        time=0.0
        for i in range(len(dist)):
            t=dist[i]/speed
            if i!=len(dist)-1:
                time+=ceil(t)
            else:
                time+=t
        return time<=hour

        