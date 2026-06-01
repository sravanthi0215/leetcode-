class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=(-inf)  
        cursum=0
        for i in nums:
            cursum+=i
            maxsum=max(cursum,maxsum)
            if cursum<0:
                cursum=0
        return maxsum   
        