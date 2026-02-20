class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        count=0
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i]==text2[j]:
                    i+=1
                    j+=1
                    count+=1
                else:
                    j+=1
                           
        return count