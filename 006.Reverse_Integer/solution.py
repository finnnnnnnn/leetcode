#!python3

class Solution:
    def reverse(self,x):
        """
        :type x:int
        :rtype:int
        """

        l=len(str(abs(x)))
        s=0
        y=abs(x)
        sum=0
        n=0
        while  l!=0:
            s,y=divmod(y,10**(l-1))
            sum+=s*(10**n)
            l=l-1
            n=n+1

        if x>0:
            return sum
        else:
            return -sum

if __name__=="__main__":
    print("reverse(123)=",Solution().reverse(123))
    print("reverse(120)=",Solution().reverse(120))
    print("reverse(-123)=",Solution().reverse(-123))
