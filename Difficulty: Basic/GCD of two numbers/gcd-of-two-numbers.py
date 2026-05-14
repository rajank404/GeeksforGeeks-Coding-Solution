import math
class Solution:
    def gcd(self, a, b):
        # code here
        # result = 1
        # if a < b:
        #     small = a
        # else:
        #     small = b
            
        # for i in range(1,small+1):
        #     if a % i == 0 and b % i == 0:
        #         result = i
        # return result
        
        if b == 0:
            return a
        else:
            return math.gcd(b,a%b)