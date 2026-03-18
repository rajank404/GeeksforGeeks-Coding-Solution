class Solution:

    def getXor(self, nums, a, b):
        ans = 0
        for i in range(a, b + 1):
            ans = ans ^ nums[i]
        return ans