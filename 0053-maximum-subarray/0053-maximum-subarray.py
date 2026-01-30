class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=float('-inf')
        csum=0
        for num in nums:
                csum+=num
                maxsum=max(csum,maxsum)
                if csum<0:
                    csum=0
        return maxsum