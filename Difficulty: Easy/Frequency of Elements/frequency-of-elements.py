class Solution:
    def countFreq(self, arr):
        #code here
        temp = {}
        for i in arr:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
                
        return [[i,count] for i,count in temp.items()]