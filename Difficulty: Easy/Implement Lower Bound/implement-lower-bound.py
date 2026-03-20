class Solution:
    def lowerBound(self, arr, target):
        # code here
        
        # m--- 1
        
        # for i in range(len(arr) -1):
        #     if arr[i] >= target:
        #         return i
        #     elif arr[i] <= target and arr[i+1] >= target:
        #         return i+1
        # return len(arr)
        
        
        # m -- 2
        
        l = 0
        h = len(arr) - 1
        ans = len(arr)
        while l <= h:
            mid = l + (h-l)// 2
            if arr[mid] >= target:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        return ans