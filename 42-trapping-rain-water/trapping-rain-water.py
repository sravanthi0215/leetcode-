class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        r=n-1
        l=w=lmax=rmax=0
        while l<r:
            if height[l]<height[r]:
                w+=max(0,lmax-height[l])
                lmax=max(lmax,height[l])
                l+=1
            else:
                w+=max(0, lmax - height[r])
                lmax=max(lmax, height[r])
                r-=1         
        return w
                

            
         
        
        