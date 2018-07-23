#!python

class Solution:
    def checkRecord(self,s):
        """
        :type s:str
        :rtype:bool
        """
        a,l=0,0
        for i in range(len(s)):
            if s[i]=='A':
                a+=1
            elif s[i]=='L' and i<=len(s)-3:
                l+=1
                if s[i+1]=='L' and s[i+2]=='L':
                    return False
                else:
                    return True
        if a<=1:
            return True
        else:
            return False

if __name__=='__main__':
    print(Solution().checkRecord("PPALLP"))
    print(Solution().checkRecord("PPALLL"))

                
