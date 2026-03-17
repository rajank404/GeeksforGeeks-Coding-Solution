class Solution:
    def countFreq(self, arr, target):
        # code here
        temp = {}
        for i in arr:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        for i,j in temp.items():
            if i == target:
                return j
        return 0
        