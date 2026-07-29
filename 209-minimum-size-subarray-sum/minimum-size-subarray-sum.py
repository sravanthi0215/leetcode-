class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        n=len(nums)
        count=float('inf')
        sum=0
        for right in  range(n):
            sum+=nums[right]
            while(sum>=target):
                count=min(count,right-left+1)
                sum-=nums[left]
                left+=1
        if count==float('inf'):
            return 0
        return count
        