#!python3

class Solution:
    def threeSum(self,nums):
        """
        :type nums:list[int]
        :rtype:List[list[int]]
        """
        result=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j,k=i+1,len(nums)-1
            while j<k:
                sums=nums[i]+nums[j]+nums[k]
                if sums>0:
                    k=k-1
                elif sums<0:
                    j=j+1
                else:
                    result.append((nums[i],nums[j],nums[k]))
                    while j<k and nums[j]==nums[j+1]:
                        j=j+1
                    while j<k and nums[k]==nums[k-1]:
                        k=k-1
                    j=j+1
                    k=k-1
        return result

if __name__=="__main__":
    nums=[-1,0,1,2,-1,-4]
    print(Solution().threeSum(nums))






