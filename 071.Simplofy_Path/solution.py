#!python3

class Solution:
    def simplifyPath(self,path):
        """
        :type:str
        :rtype:str
        """
        stack=[]
        path=path.split('/')
        for var in path:
            if var in ( '','.'):
                continue
            elif var == '..':
                if stack: stack.pop()
            else:
                stack.append(var)
        return stack

if __name__=='__main__':
    print(Solution().simplifyPath('/a/./b/../../c/'))
