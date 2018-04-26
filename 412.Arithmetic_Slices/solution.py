#!python3

class Solution:
    def numberOfArithmeticSlices(self,A):
        """
        :type A: List[int]
        :rtype: int
        """
        num=0
        cn=0
        l=len(A)
        for i in range(2,l):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                cn+=1
                num+=cn
            else:
                cn=0
        return num

if __name__=='__main__':
    A=[1,3,5,8,11,14]
    print(Solution().numberOfArithmeticSlices(A))

