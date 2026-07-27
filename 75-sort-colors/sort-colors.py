class Solution:
    def sortColors(self, nums: List[int]) -> None:

        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=0
        left=0
        right=n-1
        while(left<=right):
            if nums[left]==0:
                nums[i],nums[left]=nums[left],nums[i]
                i+=1
                left+=1
            elif nums[left]==1:
                left+=1
            else:
                nums[right],nums[left]=nums[left],nums[right]
                right-=1
                    
                    