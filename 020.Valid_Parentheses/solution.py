#!python3

class Solution:
    def isValid(self,s):
        """
        :type s:str
        :rtype:bool
        """
        l=len(s)
        t=[]
        for i in range(l):
            if s[i]=='(':
                t.append(')')
            elif s[i]=='[':
                t.append(']')
            elif s[i]=='{' :
                t.append('}')
            elif t.pop()!=s[i]:
                return False
        return len(t)==0

if __name__=='__main__':
    s='{[]}'
    print(Solution().isValid(s))


