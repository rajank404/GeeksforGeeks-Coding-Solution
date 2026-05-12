class Solution:
    def isPalindrome(self, x):
		# code here
	    reverse_digit = 0
        x_copy = x
		
		x_isneg = x < 0
		if x_isneg:
		    x = -x
        
      
        while x > 0:
            digit = x % 10
            reverse_digit = reverse_digit * 10 + digit
            x = x // 10
        
        if x_isneg:
            reverse_digit = -reverse_digit
        
        if x_copy == reverse_digit:
            return True
        return False