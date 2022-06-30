
#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        current_sum=arr[0]
        low=0
        high=0
        
        while high<n:
            
            if current_sum==s:
               return([low+1,high+1])
            elif current_sum<s:
                high+=1
                if high==n:
                    break
                current_sum+=arr[high]
            else:
                current_sum-=arr[low]
                low+=1
           
        return[-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends