class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        count1=0
        for i in nums:
            if i==1:
                count+=1
                if count>count1:
                    count1=count
            else:
                count=0
        return count1
        