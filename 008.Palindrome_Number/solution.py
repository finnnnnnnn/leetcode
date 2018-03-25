#!python3

class Solution:
    def isPalindrome(self,x):
        """
        :type x:int
        :rtype:bool
        """
        y=0
        s,t=divmod(x,10)
        if x<0:
            return False
        while s!=0:
            s,y=divmod(s,10)
            t=t*10+y
        return x==t

if __name__=="__main__":
    print("123321",Solution().isPalindrome(123321))
    print("1221",Solution().isPalindrome(1221))
    print("1231",Solution().isPalindrome(1231))
    print("-1221",Solution().isPalindrome(-1221))
        
            
            


