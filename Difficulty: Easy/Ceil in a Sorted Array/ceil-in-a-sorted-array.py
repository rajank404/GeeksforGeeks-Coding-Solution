#User function Template for python3
class Solution:
    def findCeil(self, arr, target):
        # code here
        l = 0
        h = len(arr) - 1
        ans = -1
  
        while l <= h:
            mid = l + (h-l) // 2
            if arr[mid] >= target:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        return ans
