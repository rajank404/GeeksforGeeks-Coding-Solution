class Solution:
    def findFloor(self, arr, target):
        # code here
        l = 0
        h = len(arr) - 1
        ans = -1
  
        while l <= h:
            mid = l + (h-l) // 2
            if arr[mid] <= target:
                l = mid + 1
                ans = mid
            else:
                h = mid - 1
        return ans
      
