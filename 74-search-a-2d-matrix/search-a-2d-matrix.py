class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        top=0
        bottom=m-1
        validrow=-1
        while(top<=bottom):
            mid=(top+bottom)//2
            if matrix[mid][0] <= target <= matrix[mid][n-1]:
                validrow=mid
                break
            elif target<matrix[mid][0]:
                bottom=mid-1
            else:
                top=mid+1
        if validrow==-1:
            return False
        left=0
        right=n-1
        while(left<=right):
            mid1=(left+right)//2
            if matrix[validrow][mid1]==target:
                return True
            elif matrix[validrow][mid1]<target:
                left=mid1+1
            else:
                right=mid1-1
        return False
        