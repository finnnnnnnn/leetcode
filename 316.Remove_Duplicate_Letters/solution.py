#!python3

class Solution:
    def removeDuplicateLetters(self,s):
        """
        :type s:str
        :rtype:str
        """
        sl=list(s)
        slist=[]
        l=len(s)
        while len(sl)!=len(set(sl)):
            for i in range(l):
                if i>=1:
                    if sl[i]<sl[i-1]:
                        if sl[i-1] in sl[i:]:
                            slist.pop()
                            slist.append(sl[i])
                        else:
                            slist.append(sl[i])
                    else:
                        slist.append(sl[i])
                else:
                    slist.append(sl[i])
            l=len(slist)
            if slist[-1] in slist[0:-1]:
                slist.pop()
            sl=slist
            slist=[]
        return sl

if __name__=='__main__':
    s='cbacdcbc'
    print(Solution().removeDuplicateLetters(s))
