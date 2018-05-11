#!python3

class Solution:
    def dailyTemperatures(self,temperatures):
        """
        :type:temperatures: List[int]
        :rtype: List[int]
        """
        stack=[]
        l=len(temperatures)
        res=[0]*len(temperatures)
        for i in range(l-1,-1,-1):
            if len(stack)==0:
                stack.append(temperatures[i])
            elif stack[-1]>temperatures[i]:
                res[i]=1
                stack.append(temperatures[i])
            else:
                j=i+1
                while stack[-1]<=temperatures[i] and len(stack)!=1:
                    res[i]+=res[j]
                    stack.pop()
                    j+=1
                if len(stack)==1 and stack[-1]<temperatures[i]:
                    res[i]=0
                    stack.pop()
                else:
                    res[i]+=1
                stack.append(temperatures[i])
        return res

if __name__=='__main__':
    temps=[73,74,75,71,69,72,76,73]
    print(Solution().dailyTemperatures(temps))

