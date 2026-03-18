class Solution:
    def upperBound(self, arr, target):
        # code here
        l = 0
        h = len(arr) - 1
        ans = len(arr)
        while l <= h:
            mid = l + (h-l) // 2
            if arr[mid] > target:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        return ans
        