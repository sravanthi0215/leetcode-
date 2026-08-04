class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
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
        return max(maxsum,-minsum)
        