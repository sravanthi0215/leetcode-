class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        count=defaultdict(int)
        left=0
        maxlength=0
        n=len(fruits)
        for right in range(n):
            count[fruits[right]]+=1
            while(len(count)>2):
                count[fruits[left]]-=1
                if count[fruits[left]]==0:
                    del count[fruits[left]]
                left+=1
            maxlength=max(maxlength,right-left+1)
        return maxlength

        