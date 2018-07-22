#!python3

class Solution:
    def generate(self,numRows):
        """
        :type numRows:int
        :rtype:List[List[int]]
        """
        res=[]
        row=[1]
        for i in range(numRows):
            res.append(row)
            row=[1]+[row[j-1]+row[j] for j in range(1,len(row))]+[1]
        return res

if __name__=='__main__':
    print(Solution().generate(5))
