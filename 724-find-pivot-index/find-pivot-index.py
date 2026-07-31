class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum=0
        for i in range(len(nums)):
            totalsum+=nums[i]
        leftsum=0
        for i in range(len(nums)):
            rightsum=totalsum-nums[i]-leftsum
            if leftsum==rightsum:
                return i
            leftsum+=nums[i]
        return -1