#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#emmm,not O(log(m+n))
class Solution:
    def findMedianSortedArrays(self,nums1,nums2):
        """
        :type n1:List[int]
        :type n2:List[int]
        :rtype:float
        """
        sNums1,sNums2=sorted(nums1),sorted(nums2)
        l1,l2=len(nums1),len(nums2)
        mins,maxs=0,0
        if l1==1:
            min1=0
            max1=sNums[0]
        elif l1%2==0:
            min1=sNums1[l1/2-1]
            max1=sNums1[l1/2]
        else:
            min1=sNums1[(l1-1)/2-1]
            max1=sNums1[(l1-1)/2]

        if l2==1:
            min2=sNums2[0]
            max2=0
        elif l2%2==0:
            min2=sNums2[l2/2-1]
            max2=sNums2[l2/2]
        else:
            min2=sNums2[(l2-1)/2]
            max2=sNums2[(l2-1)/2+1]
        if min1<min2:
            mins=min1
        else:
            mins=min2
        if max1>max2:
            maxs=max1
        else:
            maxs=max2
        return (float(mins)+float(maxs))/2

if __name__=="__main__":
    nums1=[1,3]
    nums2=[2]
    nums3=[1,2]
    nums4=[3,4]
    print(Solution().findMedianSortedArrays(nums1,nums2)==2.0)
    print(Solution().findMedianSortedArrays(nums3,nums4)==2.5)
