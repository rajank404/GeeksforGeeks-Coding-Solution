class Solution:
    def lowerBound(self, arr, target):
        # code here
        for i in range(len(arr) -1):
            if arr[i] >= target:
                return i
            elif arr[i] <= target and arr[i+1] >= target:
                return i+1
        return len(arr)
        