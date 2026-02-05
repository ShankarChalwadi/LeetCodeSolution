class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        return s==t
        '''if len(s)!=len(t):
            return False
        return sorted(s)==sorted(t)'''

        