class Solution:
    def countDigits(self, n):
        # code here
        result = list(map(int,str(n)))
        return len(result)
