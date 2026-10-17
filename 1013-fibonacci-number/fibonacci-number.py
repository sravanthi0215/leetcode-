class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        prev0=0
        prev1=1
        for i in range(2,n+1):
            temp=prev0+prev1
            prev0=prev1
            prev1=temp
        return prev1

        