class Solution:
    def searchInsertK(self, arr, k):
        # code here
        l = 0
        h = len(arr)-1
        ans = len(arr)
        while l <= h:
            mid = l + (h-l)//2
            if arr[mid] >= k:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        return ans
        