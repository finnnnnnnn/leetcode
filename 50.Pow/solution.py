#!python3

class Solution:
    def myPow(self,x,n):
        """
        :type x:float
        :type n:int
        :rtype:float
        """
        l1=len(str(x))
        l2=len(str(int(x)))
        if int(x-1) in range(-100,100) and n in range(-32,32):
            return ((x*(10**(l1-l2-1)))**n)/((10**(l1-l2-1))**n)
        else:
            return None

if __name__=='__main__':
    print(Solution().myPow(2.1,2))
