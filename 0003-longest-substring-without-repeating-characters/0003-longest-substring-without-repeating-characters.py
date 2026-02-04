class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl=0
        l=0
        uniqset=set()
        for r in range(len(s)):
            while s[r] in uniqset:
                uniqset.remove(s[l])
                l+=1
            uniqset.add(s[r])
            maxl=max(maxl,r-l+1)
        return maxl         