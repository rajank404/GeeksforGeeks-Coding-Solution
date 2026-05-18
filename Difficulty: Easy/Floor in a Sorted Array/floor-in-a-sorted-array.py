class Solution:
    def findFloor(self, arr, x):
        # code here
        l = 0
        ans = -1
       
        h = len(arr) - 1
        while l <= h:
            mid = l+ (h-l)//2
            if arr[mid] <= x:
                ans = mid
                l = mid + 1
            else:
                h = mid - 1
        return ans
        