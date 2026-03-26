class Solution:
    def floorSqrt(self, x): 
        # code here
        
        # brute force (Linear Search)
        
        
        # ans = 1
        # for i in range(1,n):
        #     if i*i <= n:
        #         ans = i
        #     else:
        #         break
        # return ans
        
        l = 0
        h = x
        ans = 1
        while l <= h:
            mid = l+(h-l)//2
            temp = mid*mid
            if temp == x:
                return mid
            elif temp < x:
                l = mid + 1
                ans = mid
            else:
                h = mid - 1

        return ans
        
                
        