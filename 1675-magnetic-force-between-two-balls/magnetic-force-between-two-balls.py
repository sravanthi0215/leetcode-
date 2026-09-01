class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low=1
        high=max(position)-min(position)
        ans=0
        while(low<=high):
            gap=low+(high-low)//2
            if self.canPlace(position,m,gap):
                ans=gap
                low=gap+1
            else:
                high=gap-1
        return ans
    def canPlace(self,position,m,gap):
        curr=position[0]
        count=1
        for i in range(1,len(position)):
            if position[i]-curr>=gap:
                count+=1
                curr=position[i]
        if count>=m:
            return True
        else:
            return False





        