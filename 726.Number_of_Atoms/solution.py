#!python3

class Atom:
    def __init__(self,name,count):
        self.name=name
        self.count=count
    def getCount(self):
        return self.count
    def getName(self):
        return self.name
class Solution:
    def countOfAtoms(self,formula):
        """
        :type formula:str
        :rtype:str
        """
        res=''
        res_name=''
        i,l=0,len(formula)
        stack=[]
        flag=[]
        while i<l:
            c=formula[i]
            if c.isalpha()==True:
                if c>='A' and c<='Z':
                    atom=Atom(c,1)
                    stack.append(atom)
                    if formula[i-1]=='(':
                        flag.append(len(stack)-1)
            elif c.isdigit()==True:
                appC=int(c)-1
                stack[-1].count=stack[-1].count+appC
            elif c=='(':
                pass
            elif c==')':
                cnt=int(formula[i+1])
                stack_len=len(stack)
                for j in range(flag.pop(),stack_len):
                    stack[j].count=stack[j].count*cnt
                i+=1
            i+=1
        
        for i in range(len(stack)):
            if stack[i].name not in res_name:
                res_name+=stack[i].name
            else:
                stack[res_name.find(stack[i].name)].count+=stack[i].count
                stack.pop(i)
        for i in range(len(stack)):
            s=stack[i].name+str(stack[i].count)
            res+=s
        return res
        
if __name__=='__main__':
    formula='K4(ON(SO3)2)2'
    print(Solution().countOfAtoms(formula))


