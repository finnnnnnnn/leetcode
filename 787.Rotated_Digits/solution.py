#!python3

class Solution:
    def rotatedDigits(self,N):
        """
        :type N:int
        :rtype:int
        """
        n=N
        s=str(n)
        l,i=0,0
        nums,f=1,0
        while s.find('1')!=-1 or s.find('0')!=-1:
            if s.find('1')!=-1:
                i=len(s)-s.find('1')
                n,t=divmod(n,10**(i-1))
                n=n*10**(i-1)-1
                s=str(n)
            else:
                i=len(s)-s.find('0')
                n,t=divmod(n,10**(i-1))
                n=n*10**(i-1)-1
                s=str(n)
        slist=list(s)
        for i in range(len(s)):
            temp=int(slist[i])
            if i>=1:
                f=f+4**i
            if temp==9:
                nums=nums*4
            elif temp>=6:
                nums=nums*3
            elif nums==5:
                nums=nums*2
            else:
                nums=nums*1
        return nums+f
if __name__=='__main__':
    print(Solution().rotatedDigits(4351))
