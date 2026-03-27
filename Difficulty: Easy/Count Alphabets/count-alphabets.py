#User function Template for python3

class Solution:

    def Count(self, S):
        # code here
        s = ""
        for i in S:
            if i >= "a" and i <= "z" or i >= "A" and i <= "Z":
                s = s + i
        return len(s)