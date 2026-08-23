class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return(self.find_first(nums,target),self.find_last(nums,target))
    def find_first(self,nums,target):
        l,r=0,len(nums)-1
        ans=-1
        while(l<=r):
            mid=l+(r-l)//2
            if nums[mid]==target:
                ans=mid
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return ans
    def find_last(self,nums,target):
        l,r=0,len(nums)-1
        ans=-1
        while(l<=r):
            mid=l+(r-l)//2
            if nums[mid]==target:
               ans=mid
               l=mid+1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return ans




        