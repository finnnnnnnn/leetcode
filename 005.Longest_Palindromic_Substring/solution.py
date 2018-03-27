#!/usr/bin/env python3

#a bit of problem

class Solution:
    def longestPalindrome(self,s):
        """
        :type s:str
        :rtype:str
        """
        strLen=len(s)
        flag=True
        start,end,index,length,k=0,0,0,0,0
        for i in range(0,strLen):
            if s[i+1:].find(s[i]):
                start=i
                j=s.rindex(s[i])
                end=j
                flag=True
                while flag and(start<end):
                    start=start+1
                    end=end-1
                    if s[start]!=s[end]:
                        flag=False
                if flag==True:
                    k=j-i+1
                    if k>length:
                        length=k
                        index=i
        return s[index:index+length]

if __name__=="__main__":
    print(Solution().longestPalindrome("adda")=="adda")
    print(Solution().longestPalindrome("babad")=="bab")
    print(Solution().longestPalindrome("dassessae")=="assessa")
    print(Solution().longestPalindrome("deedfgfdee")=="eedfgfdee")
    print(Solution().longestPalindrome("livevil")=="livevil")

