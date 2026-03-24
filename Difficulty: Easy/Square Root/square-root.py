class Solution:
    def floorSqrt(self, n): 
        # code here
        ans = 1
        for i in range(1,n):
            if i*i <= n:
                ans = i
            else:
                break
        return ans
                
        