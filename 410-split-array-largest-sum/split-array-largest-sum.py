class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k>n:
            return -1
        def issafe(limit):
            stu=1
            pages=0
            for book in nums:
                if book+pages<=limit:
                    pages+=book
                else:
                    stu+=1
                    pages=book
                if stu>k:
                    return False
            return True
        low=max(nums)
        high=sum(nums)
        ans=high
        while low<=high:
            mid=(low+high)//2
            if issafe(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        
        