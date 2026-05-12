#User function Template for python3

class Solution:
	def reverseDigits(self, n):
		# Code here
		result = ""
		while n > 0:
		    digit = n % 10
		    result = result + str(digit)
		    n = n // 10
		return int(result)
		    