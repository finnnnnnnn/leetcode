#!python3

class Solution:
    def lengthOfLongestSubstring(self,s):
        """
        :type s:str
        :rtype:int
        """
        i=0
        length=0
        t=0
        list=[]
        for i in range(0,len(s)):
            list.append(s[i])
            for j in range(i+1,len(s)):
                if  s[j] in list[i:j]:
                    t=len(list[i:j])
                    if t>length:
                        length=t
                    list.append(s[j])
                    i=i+list[i:j].index(s[j])+1
                    break
                else:
                    list.append(s[j])
                    t=len(list[i:j+1])
                    if t>length:
                        length=t
        return length


if __name__=="__main__":
    print("abcabcbb:",Solution().lengthOfLongestSubstring("abcabcbb"))
    print("abcbefgdcbb",Solution().lengthOfLongestSubstring("abcbefgdcbb"))
    print("bbbbb",Solution().lengthOfLongestSubstring("bbbbb"))
    print("pwwkew",Solution().lengthOfLongestSubstring("pwwkew"))


