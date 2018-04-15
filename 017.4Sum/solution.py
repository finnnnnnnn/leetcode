#!python3

import datetime

class Solution:
    def fourSum(self,nums,target):
        """
        :type nums:list[int]
        :type target:int
        :rtype:List[list[int]]
        """
         
        nums.sort()
        result=[]
        l=len(nums)
        if l<4:
            return result
        maxn,a=nums[l-1],0
        if 4*maxn<target or 4*nums[0]>target:
            return result
        for i in range(l-3):
            a=nums[i]
            if i>0 and a==nums[i-1]:
                continue
            if a+3*maxn<target:
                continue
            if 4*a>target:
                break
            if 4*a==target:
                if i+3<l and nums[i+3]==a:
                    result.append((a,a,a,a))
                break
            threenums=nums[(i+1-l):]
            target1=target-a
            l2=len(threenums)
            
            for j in range(l2-2):
                b=threenums[j]
                if j>0 and b==nums[j-1]:
                    continue
                if b+2*maxn<target1:
                    continue
                if 3*b>target1:
                    break
                if 3*b==target1:
                    if threenums[j+2]==b:
                        result.append((a,b,b,b))
                    break
                twonums=threenums[(j+1-l2):]
                target2=target1-b
                if 2*twonums[0]>target2 or 2*twonums[-1]<target2:
                    break
                m,n,sums=0,len(twonums),0
                for p in range(n-1):
                    for q in range(p+1,n):
                        sums=twonums[p]+twonums[q]
                        if sums==target2:
                            result.append((a,b,twonums[p],twonums[q]))

        return result
            

        
if __name__=="__main__":
    start=datetime.datetime.now()
    nums=[1,0,-1,0,-2,2]
    print(Solution().fourSum(nums,0))
    end=datetime.datetime.now()
    print((end-start).microseconds,"ms")


