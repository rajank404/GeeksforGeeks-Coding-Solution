#User function Template for python3

class Solution:
    def getDivisors(self, N):
        # code here
        
        # Naive solution
        
        # for i in range(1,N+1):
        #     if N % i == 0:
        #          print(i,end=" ")
        
        # optimal solution
        temp = []
        for i in range(1,int(N**0.5)+1):
            if N % i == 0:
                temp.append(i)
                
                a = N//i
                if i != a:
                    temp.append(a)
        temp.sort()
        return temp
        
   
                
  
        
        
        
        
        

