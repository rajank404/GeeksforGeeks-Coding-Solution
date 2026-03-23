class Solution:
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        d = d % n
        i = 0
        j = d - 1
        while i < j:
            arr[i],arr[j] = arr[j],arr[i]
            i = i + 1
            j = j - 1
        i = d
        j = n-1
        while i < j:
            arr[i],arr[j] = arr[j],arr[i]
            i = i + 1
            j = j - 1
        i = 0
        j = n - 1
        while i < j:
            arr[i],arr[j] = arr[j],arr[i]
            i = i + 1
            j = j - 1
        return arr
            
        
            
        