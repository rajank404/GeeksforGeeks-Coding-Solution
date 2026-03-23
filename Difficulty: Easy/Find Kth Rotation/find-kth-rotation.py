class Solution:
    def findKRotation(self, arr):
        # code here
        l = 0
        h = len(arr) - 1
        ans = 1000000
        while l <= h:
            mid = l + (h-l) // 2 
            if arr[l] <= arr[mid]:
                ans = min(ans,arr[l])
                l = mid + 1
            elif arr[mid] <= arr[h]:
                ans = min(ans,arr[mid])
                h = mid - 1
        return arr.index(ans)
        
        