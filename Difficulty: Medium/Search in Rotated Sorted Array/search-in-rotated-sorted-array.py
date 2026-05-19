class Solution:
    def search(self, arr, target):
        # code here
        l = 0
        h = len(arr)-1
        while l <= h:
            mid = l+(h-l)//2
            if arr[mid] == target:
                return mid
            elif arr[l] <= arr[mid]:
                if arr[l] <= target and target <= arr[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if arr[mid] <= target and target <= arr[h]:
                    l = mid + 1
                else:
                    h = mid - 1
        return -1
        

        