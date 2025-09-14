<<<<<<< HEAD
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l=0
        res=0
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l=l+1
            charSet.add(s[i])
            res=max(res,i-l+1)
=======
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l=0
        res=0
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l=l+1
            charSet.add(s[i])
            res=max(res,i-l+1)
>>>>>>> b46ee89f4f50447a1cc104dd7e4a5aae651c9902
        return res