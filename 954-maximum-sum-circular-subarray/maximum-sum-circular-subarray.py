class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalsum=0
        for i in nums:
            totalsum+=i
        maxsum=(-inf)  
        cursum=0
        for i in nums:
            cursum+=i
            maxsum=max(cursum,maxsum)
            if cursum<0:
                cursum=0
        minsum=(+inf)
        cursum2=0
        for i in nums:
            cursum2+=i
            minsum=min(cursum2,minsum)
            if cursum2>0:
                cursum2=0
        if cursum==0:
            return maxsum
        wrapsum=0
        wrapsum=totalsum-minsum
        return max(wrapsum,totalsum,maxsum)
        
        
        

        
        